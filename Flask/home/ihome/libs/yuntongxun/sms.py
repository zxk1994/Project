#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8a216da8662360a40166586b955b10d0'

#���ʺ�Token
accountToken= 'f382ea179b9c4455badf1df3ca77e427'

#Ӧ��Id
appId='8a216da8662360a40166586b95ba10d7'

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

#����˿� 
serverPort='8883'

#REST�汾��
softVersion='2013-12-26'

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

# def sendTemplateSMS(to,datas,tempId):
#
#     #��ʼ��REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)

#sendTemplateSMS(�ֻ�����,��������,ģ��Id)


class CCP(object):
    """  �����������ĳ������ʽ,�õ���ģʽ��ֻ��ʼ��һ�ξ���"""
    #������������������
    __instance=None
    def __new__(cls, *args, **kwargs):
        #�ж�CCP��û�д����õĶ������û�У�����һ��������б���
        #����У�ֱ�ӷ��ر���Ķ���
        if cls.__instance is None:
            obj=super(CCP,cls).__new__(cls)

            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls.__instance=obj  #����һ��
        return cls.__instance

    def send_template_sms(self,to, datas, tempId):

        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # for k, v in result.iteritems():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)
        #�뷵����������
        status_code=result.get("statusCode")
        if status_code == "000000":
            #���Ͷ��ųɹ�
            return 0
        else:
            #����ʧ��
            return -1


if __name__ == "__main__":
    ccp=CCP()
    #�ֻ�����,  ��������(����[��֤������ ������ʱ������5����]),  ģ��Id������1
    ccp.send_template_sms("15231128853",["1124","5"],1)