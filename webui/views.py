import json

from django.shortcuts import render


# Create your views here.
def report(request):
    result_data = {
        "testPass": 0,
        "testResult": [],
        "testName": "自动化测试报告",
        "testAll": 0,
        "testFail": 0,
        "beginTime": "2022-05-19 22:10:33",
        "totalTime": "0s",
        "testSkip": 0,
        "testError": 0
    }
    temp={}
    # for key,val in result_data.items():
    #     try:
    #         int(result_data.get(key))
    #     except (ValueError,TypeError):
    #         temp[key]=a1.get(key)+a2.get(key)+a3.get(key)
    #     else:
    #         temp[key] = int(a1.get(key)) + int(a2.get(key)) + int(a3.get(key))
    print(temp)
    return render(request, 'report.html', {'resultData': json.dumps(temp)})
    # return render(request, 'report.html', {'resultData': json.dumps(result_data)})
