# coding=utf-8
import os


def list_files(file_path):
    file_list = []

    for root, dirs, files in os.walk(file_path):

        for fileObj in files:
            file_list.append(os.path.join(root, fileObj))

    return file_list


def chang_char(d):
    file_path = "D:/BaiduNetdiskDownload/components/"

    file_list = list_files(file_path)

    for k in d:
        for file in file_list:
            f = open(file, 'r', encoding='utf-8')
            content = f.read()
            f.close()
            # 如果字符串前后为非中文字符就替换
            locate = content.find(d[k])
            if content[locate+1] not in '[\u4e00-\u9fa5]':
                temp = content.replace(d[k], k)
                f = open(file, 'w', encoding='utf-8')
                f.write(temp)
                f.close()


if __name__ == '__main__':
    data = {
        'activeRules' : '自定义活跃统计规则',
        'userFrequency' : '按使用频次设置',
        'hour' : '小时',
        'date' : '日期',
        'type' : '型号',
        'transaction' : '次交易行为',
        'deviceActivateTreed' : '设备激活走势',
        'deviceActivateNumTreed' : '设备激活数走势',
        'reSelect' : '最大时间跨度为3个月，请重新选择日期',
        'onlineDetail' : '在线数据明细',
        'deviceActiveTrend' : '设备活跃走势',
        'active' : '活跃数',
        'online' : '在线数',
        'onlineRate' : '在线率',
        'duration' : '统计周期',
        'setDuration' : '按时长设置',
        'activateRateTrend' : '激活率走势',
        'averageOonline' : '每台设备每日平均在线时长',
        'dailyActivity' : '日活跃量',
        'SN' : '设备编号',
        'deployedRate' : '激活率',
        'activeRulemModify' : '自定义活跃统计规则修改成功',
        'item' : '对象',
        'selectTtem' : '请选择查询对象',
        'query' : '查询',
        'deployNumber': '激活数量',
        'currentRule' : '当前规则',
        'activateNumTreed' : '激活数走势',
        'dailyIncrement' : '在线跃增量',
        'deployed' : '已激活',
        'onlineDevice' : '在线设备',
        'activeTrend' : '活跃走势',
        'merchant' : '所属商户',
        'onlineDays' : '在线天数',
        'status' : '状态',
        'refund' : '退款',
        'connectNetwork' : '连接网络',
        'averageTime' : '每台设备每日平均在线时长',
        'dealFrequency' : '按交易频次设置',
        'onceOnline' : '为在线一次',
        'activateSummary': '激活数据汇总',
        'activeDays' : '活跃天数',
        'onlineSummary' : '在线数据汇总',
        'deviceType' : '设备类型',
        'onlineRule' : '自定义在线统计规则',
        'confirm' : '确定',
        'each' : '每台设备每日发生',
        'activeDay' : '为当日活跃',
        'device' : '设备',
        'communication' : '按通讯设置',
        'deploy' :  '激活数',
        'nonDeploy' : '未激活',
        'onlineRuleSuccess' : '自定义在线统计规则新增成功',
        'deployTrend' : '设备激活率走势',
        'nonActiveDays' : '不活跃天数',
        'selectDate' : '请选择日期',
        'onlineTrend' : '设备在线走势',
        'all' : '全部',
        'OfflineDays' : '脱机天数',
        'onlineRulemModify' : '自定义在线统计规则修改成功',
        'activeSummary' : '活跃数据汇总',
        'payrAndRefund' : '收、退款',
        'nonActive' : '未激活设备',
        'store' : '所属门店',
        'communicates' : '每台设备与服务器发生通讯（连接网络）视为设备活跃',
        'activeDetail' : '活跃数据明细',
        'deployedDevice' : '已激活设备',
        'offlineDevices' : '脱机设备',
        'activeRuleSuccess' : '自定义活跃统计规则新增成功',
        'devices' : '设备数',
        'quantity' : '数量',
        '30days' : '近30天活跃',
        '7days' : '近7天活跃',
        'yesterdayActive' : '昨天活跃',
        'merchants' : '商户数量',
        'deviceNumber' : '设备数量',
        'storeNumber' : '门店数量',
        'activateNumber' : '激活数量',
        'data' : '数据汇总',
        'activedDevices' : '活跃设备',
        'content' : '内容',
        'waiting' : '正在跳转',
        'logOut' : '退出登录',
        'operational' : '运营分析',
        'yesterday' : '昨日',
        'month' : '本月',
        'week' : '本周',
        'paraError' : '参数错误',
        'accountError' : '用户错误',
        'ruleInvalid' : '规则使能类型无效',
        'ruleNotExist' : '规则类型不存在',
        'serviceerror' : '服务数据错误'
    }
    data2 = {}
    for key in data:
        data2['{{$t("message.' + key + '")}}'] = data[key]

    chang_char(data2)
