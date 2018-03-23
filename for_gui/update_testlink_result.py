# encoding: utf-8
# 2018.03.17

import testlink
import time
import os


url = "http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
tester_key = {"fzq": "3c55ffa8e147e98ec9d96255b0e96e7f"}
tlc = testlink.TestlinkAPIClient(url, tester_key["fzq"])

project_name = '设备管理平台'
test_plan_name = '测试环境'
first_menu = ['设备首页', '服务商管理', '设备管理', '配置管理', '用户管理', '系统管理', '数据统计']


def to_execute_cases():
    need_run_cases = []

    # get targeted project
    projects = tlc.getProjects()
    target_project = [project for project in projects if project['name'] == project_name]

    # get targeted test plan
    test_plan = tlc.getProjectTestPlans(target_project[0]['id'])
    target_test_plan = [plan for plan in test_plan if plan['active'] == '1' and test_plan_name in plan['name']]
    target_test_plan_id = target_test_plan[0]['id']

    # get test suites info (all of the level 1 menu)
    suites = tlc.getFirstLevelTestSuitesForTestProject(target_project[0]['id'])
    # get targeted test suite id
    target_suite = [suite for suite in suites if suite['name'] in first_menu]
    # get test suite (all of function under the Level 1 menu)
    test_suite = [tlc.getTestCasesForTestSuite(target_suite[i]["id"], True, 'full') for i in range(len(target_suite))]

    # get targeted all of test cases
    target_test_cases = tlc.getTestCasesForTestPlan(target_test_plan[0]['id']).values()

    # traversal each of test case
    for case in target_test_cases:

        for case_body in case.values():
            # if test case has been run
            if not case_body['exec_on_build']:

                # get time stamp for reportTCResult
                start_time = time.time()
                time_stamp = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                duration_min = str((time.time() - start_time)/60)

                # get case information for reportTCResult in case body
                case_id = case_body["tcase_id"]
                build_information = tlc.getBuildsForTestPlan(target_test_plan[0]['id'])
                build_name = build_information[0]["name"]
                test_case_external_id = case_body['external_id']
                case_platform_name = case_body['platform_name']

                # get case result for reportTCResult
                login_name = tlc.getTestCaseAssignedTester(
                    target_test_plan[0]['id'],
                    case_body['full_external_id'],
                    buildname=build_name,
                    platformname=case_platform_name
                )

                # verify tester of execution cases
                if list(tester_key.keys())[0] == login_name[0]['login']:

                    case_name = case_body['tcase_name']
                    print(case_name)

                    # execute test case
                    os.system('python ' + case_name + '.py')
                    case_steps = tlc.getTestCase(case_body['tcase_id'])[0]['steps']

                    # collect the test case result: 'result': 'p' or 'result': 'f' marks one case result;
                    notes = open('testLink.notes', 'r', encoding='UTF-8')
                    temp = notes.read().replace('\n', '')
                    temp1 = temp.split("'result': ")

                    # result of all steps
                    test_case_result = temp1[-1][1]

                    # execution notes of all steps
                    temp3 = temp1[-2].replace("'p'", '').replace("'p'", '')
                    steps_notes = temp3.split('-*- The case is executed -*-')[:-1]

                    notes.close()

                    # if case steps length equal step notes length and test case result is 'p', the case result is pass
                    if len(steps_notes) == len(case_steps) and test_case_result == 'p':

                        test_case_step_results = [{
                            'step_number': str(j + 1),
                            'result': 'p',
                            'notes': steps_notes[j]
                        } for j in range(len(steps_notes))]

                        tlc.reportTCResult(
                            case_id, target_test_plan_id,
                            build_name,
                            test_case_result,
                            'automated test cases',
                            guess=True,
                            testcaseexternalid=test_case_external_id,
                            platformname=case_platform_name,
                            execduration=duration_min,
                            timestamp=time_stamp,
                            steps=test_case_step_results
                        )
                    elif len(steps_notes) == len(case_steps) and test_case_result == 'f':

                        test_case_step_results = [{
                            'step_number': str(j + 1),
                            'result': 'f',
                            'notes': steps_notes[j]
                        } for j in range(len(steps_notes))]

                        tlc.reportTCResult(
                            case_id, target_test_plan_id,
                            build_name,
                            test_case_result,
                            'automated test cases',
                            guess=True,
                            testcaseexternalid=test_case_external_id,
                            platformname=case_platform_name,
                            execduration=duration_min,
                            timestamp=time_stamp,
                            steps=test_case_step_results
                        )
                    else:
                        print('\nFailed updates!\n')

if __name__ == "__main__":

    to_execute_cases()
