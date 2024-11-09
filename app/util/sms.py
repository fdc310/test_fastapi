# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List
import json
import configparser

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


config = configparser.ConfigParser()


config_path = "config.ini"
config.read("", encoding="utf-8")


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        args: List[str]
    ) -> None:
        # access_key_id = str(config.get('CONFIGS','Access_key_id'))
        # sign_name = str(config.get('CONFIGS','Sign_name'))
        # print(sign_name)
        # access_key_secret = str(config.get('CONFIGS','Access_key_secret'))
        # template_code = str(config.get('CONFIGS','Template_code'))
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client("", "")
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            # phone_numbers=args[0],
            # sign_name=sign_name,
            # template_code= template_code,
            # template_param = json.dumps({"code": args[1]})
            phone_numbers=args[0],
            sign_name= "",
            template_code= "",
            template_param = json.dumps({"code": args[1]})
        )


        try:
            # 复制代码运行请自行打印 API 的返回值
            a = client.send_sms_with_options(send_sms_request, util_models.RuntimeOptions())
            print(a)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client("", "")
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers='',
            sign_name='',
            template_code='',
            template_param=json.dumps({"code": "1234"})

        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            a = await client.send_sms_with_options_async(send_sms_request, util_models.RuntimeOptions())
            print(a)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

