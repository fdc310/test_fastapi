from fastapi import APIRouter,Depends
from app.db.dataBase import Session
from app.db.model.EbUser import Session as CrmebSession
from app.db.model.EbUser import EbUser
from app.db.model.UserPointsTable import UserPointsTable
from app.db.model.ScriptDatum import ScriptDatum
from app.db.model.SpeechScript import SpeechScript
from app.util.TokenUtil import get_id

from app.util.Chatmsg import Chat_msg
from app.util.dataModel import Chat_replymeg


router = APIRouter(tags=["cahtgpt调用"])



@router.post("/chat_replymeg",summary="chat_replymeg")
async def chat_replymeg(item:  dict,user_id : int = Depends(get_id)):
    # user_id = get_user_id()
    print(user_id, type(user_id))
    data = item
    try:
        retlue = vip_logic(data, user_id, reply_prompt_join)
        return retlue


    except Exception as e:
        print(str(e))
        return {'message': 'error', 'status': 10000}

@router.post('/chat_copymeg',summary='chat_copymeg')
async def chat_copymeg(item:  dict,user_id : int = Depends(get_id)):
    print(user_id, type(user_id))
    data = item
    try:
        retlue = vip_logic(data,user_id,copy_prompt_join)
        return retlue

    except Exception as e:
        print(str(e))
        return {'message':'error','status':10000}


@router.post('/chat_live',summary='chat_live')
async def chat_copymeg(item:  dict,user_id : int = Depends(get_id)):
    print(user_id, type(user_id))
    data = item
    try:
        retlue = vip_logic(data,user_id,live_pormpt_join)
        return retlue

    except Exception as e:
        print(str(e))
        return {'message':'error','status':10000}




def vip_logic(data, user_id, func):
    crmeb_session = CrmebSession()
    session = Session()
    try:

        user_id = int(user_id)
        user_jurisdiction = crmeb_session.query(EbUser).filter_by(user_id=user_id, del_flag=0).first()
        user_points = session.query(UserPointsTable).filter(UserPointsTable.userId == user_id,
                                                            UserPointsTable.isDeleted == 0).first()
        if user_jurisdiction.user_type == '1':
            retlue = func(data, user_id)
            spee_script_add = SpeechScript(userId=user_id, scriptText='文本生成消耗', consumption=1)
            session.add(spee_script_add)
            session.commit()
        else:

            if user_points.remainingDuration > 0:
                print(user_points.remainingDuration)
                retlue = func(data, user_id)

                user_points.remainingDuration -= 1
                session.commit()
                # spee_script_add = SpeechScript(userId=user_id, scriptText='文本生成消耗', consumption=1)
                # session.add(spee_script_add)
                # session.commit()

            else:
                retlue = {'message': '你的免费次数已用尽，如需继续使用请充值', 'status': 300}
        return retlue
    except Exception as e:
        print(str(e))
        return {'message': 'error', 'status': 10000}
    finally:
        session.close()
        crmeb_session.close()





def live_pormpt_join(data,userid):
    # global roles_str1,roles_str_set,role_str_set,enterprise_str_set,script_style_set,set_meal_set,products_str_set,shope_set

    role_str1 = '你现在扮演的是{},'
    role_str2 = '叫{}，'
    role_str3 = '性别{}，'
    role_str10 = '人物风格是{},'
    roles_str1 = '你现在分别要扮演两个角色，分别是{}和{},'
    roles_str2 = '{}'
    enterprise_str = '我们的企业叫{}'
    enterprise_str1 = '{}，'
    enterprise_str2 = '服务特色有{}，'
    products_str = '我们的产品有{}，'
    products_str1 = '{}，'
    products_str2 = '核心特色{}，'
    products_str3 = '价格{}，'
    shope_str = '店铺名称是：{},'
    shope_str1 = '店铺所属行业：{},'
    shope_str2 = '店铺在所地址：{},'
    set_meal_str = '我们的{}链接'
    set_meal_str1 = '是{}套餐'
    set_meal_str2 = '{}'
    set_meal_str3 = '正常价格为{}'
    set_meal_str4 = '但是我们现在搞优惠，优惠力度是{}'
    role_str_set = {'role': role_str1, 'name': role_str2, 'gender': role_str3, 'role_type': role_str10}  # 对应的单角色语句字典
    roles_str_set = {'role': roles_str2, 'name': role_str2, 'gender': role_str3, 'role_type': role_str10}  # 多角色语句字典
    enterprise_str_set = {'name': enterprise_str, 'basics_massage': enterprise_str1, 'style': enterprise_str2}  # 企业语句字典
    products_str_set = {'name': products_str, 'massage': products_str1, 'style': products_str2,
                        'pirce': products_str3}  # 产品语句字典
    shope_set = {'name': shope_str, 'indnstry': shope_str1, 'address': shope_str2}  # 商铺语句字典
    set_meal_set = {'name': set_meal_str1, 'url_txt': set_meal_str, 'described': set_meal_str2, 'price': set_meal_str3,
                    'discount': set_meal_str4}  # 套餐语句字典
    script_style_set = {'武侠风': '金庸', '文学风': '董永辉', '浪漫主义': '张爱玲', '相声风': '郭德纲或者于谦', '美食介绍风': '舌尖上的中国'}  # 话术风格对应字典
    end_str = ''
    crmeb_session = CrmebSession()
    session = Session()

    print(data)
    # user_id = get_user_id()
    q_id = data.get('q_id')
    title = data.get('title')
    roles = data.get('roles')  # 角色信息列表包list
    enterprise = data.get('enterprise')  # 企业信息set
    shope = data.get('shope')  # 商铺信息set
    set_meal = data.get('set_meal')  # 套餐信息list包map
    products = data.get('products')  # 产品信息list包map
    script_style = data.get('script_style')  # 话术风格str
    try:
        if q_id:  # 这个是继续生成直播话术的时候
            title, reply = session.query(ScriptDatum.question, ScriptDatum.reply).filter(
                ScriptDatum.questionId == q_id).first()  # 查询标题和内容
            prompt = '基于之前对话接着再来20句不同的对话'  # 输入
            print(reply)
            newreply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
            if "error" in newreply:
                return {'message': 'error', 'status': 200, }  # 当chat出现error时的处理，返回状态
            else:
                updated_reply = reply + "\n" + newreply  # 做文本添加，但是只有回复？

                # 找到相应的记录并更新reply字段
                session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update({'reply': updated_reply})
                session.commit()
                return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': newreply}}  # 将恢复传给前端
        else:
            if len(roles) > 1:  # 当角色大于一个的时候进行双人设拼接
                prompt = roles_str1.format(roles[0]['role'], roles[1]['role'])  # 提取出列表中的两个角色并填充到prompt中
                prompt = str_fill(prompt, roles, roles_str_set)  # 将剩下的部分通过方法填充

                end_str = f'据以上信息编写20句对话直播间话术脚本。不能出现直播违禁词包括但不限于（' \
                          f'包含“最”及相关词语,包含“一”及相关词语，包含“级/极”及相关词语，包含“首/家/国”及相关词语，表示权威的禁忌词，' \
                          f'虚假承诺和高风险诱导类的，表示绝对、极限且无法考证的词语，涉迷信宣传的，与欺诈有关 涉嫌欺诈消费者，医疗器械/滋补膳食/保健食品类商品' \
                          f'），要保证每个段落内容丰满，你给的数据中做好标记以便我做不同角色语句分割,' \
                          f'格式示例“{roles[0]["role"]}{roles[0]["name"]}:balabala.\n{roles[1]["role"]}{roles[1]["name"]}:balabala.....”'  # 结尾语句
            else:  # 否则就单人
                prompt = ''
                prompt = str_fill(prompt, roles[0], role_str_set)  # 直接使用方法填充prompt
                end_str = '请根据信息编写至少20句话直播话术脚本。不能出现直播违禁词包括但不限于（' \
                          f'包含“最”及相关词语,包含“一”及相关词语，包含“级/极”及相关词语，包含“首/家/国”及相关词语，表示权威的禁忌词，' \
                          f'虚假承诺和高风险诱导类的，表示绝对、极限且无法考证的词语，涉迷信宣传的，与欺诈有关 涉嫌欺诈消费者，医疗器械/滋补膳食/保健食品类商品' \
                          f'），要保证每个段落内容丰满。你给的数据中做好标记以便我做语句分割' \
                          f'示例格式"{roles[0]["role"]}{roles[0]["name"]}:大家好！欢迎来到这里！\n' \
                          f'{roles[0]["role"]}{roles[0]["name"]}:今天带来的是巴里巴里。"'  # 结尾

            if enterprise:  # 填充企业信息
                prompt = str_fill(prompt, enterprise, enterprise_str_set)
            if shope:  # 填充商铺信息
                prompt = str_fill(prompt, shope, shope_set)
            if products:  # 填充产品信息
                add_pro = ''
                prompt = str_fill(prompt, products, products_str_set)
                prompt += add_pro
            if set_meal:  # 填充套餐信息
                prompt = str_fill(prompt, set_meal, set_meal_set)
            if script_style:  # 填充回复风格信息
                txt_style = script_style_set.get(script_style)
                if txt_style:  # 选择的风格做对应的填充
                    text_style = f'脚本风格为{txt_style}的{script_style}'
                else:  # 自填风格直接填充
                    text_style = f'脚本风格为{script_style}'
                prompt += text_style
            prompt += end_str  # 加上结尾词
            add_txt = ScriptDatum(
                question=title,
                analyzedReply=prompt,
                userId=1
            )  # 将prompt写入数据库
            session.add(add_txt)
            session.commit()
            q_id = add_txt.questionId  # 查询出pormptid来进行参数传递
            print(prompt)
            reply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
            if "error" in reply:  # chat出错后返回报错
                return {'message': 'error', 'status': 200, }
            else:
                session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update(
                    {'reply': reply})  # 将chat回复的文本更新至对应的prompt中
                session.commit()
            print(prompt)
            print(reply)
        return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': reply}, 'prompt': prompt}
    except Exception as e:
        print(str(e))
        return {"message":"error", "status":400}
    finally:
        session.close()





def copy_prompt_join(data,user_id):
    q_id = data.get('q_id')
    title = data.get('title')
    crmeb_session = CrmebSession()
    session = Session()
    copy_prompt = data.get('prompt')  # 输入
    copy_style = data.get('copy_style')  # 文案风格
    copy_title = data.get("copy_title") # 文案主题
    copy_describe = data.get('copy_describe') # 文案描述
    if q_id:
        title, reply = session.query(ScriptDatum.question, ScriptDatum.reply).filter(
            ScriptDatum.questionId == q_id).first()
        prompt = '基于之前对话接着再生成多不同但类似文案'
        print(reply)
        newreply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
        if "error" in newreply:
            return {'message': 'error', 'status': 200, }
        else:
            updated_reply = reply + "\n" + newreply

            # 找到相应的记录并更新reply字段
            session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update({'reply': updated_reply})
            session.commit()
            return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': newreply}}
    else:
        if copy_prompt:
            prompt = f"{copy_prompt}，请结合{copy_describe}在保留文本的原始内容的含义情况下生成一篇新的文案"
        else:
            prompt = f'请使用抖音短视频文案风格用中文编辑以下文案，文案的主题是{copy_title}，我希望你用{copy_style}文案风格来撰写此次文案，' \
                 f'请务必保持{copy_describe}内容的原始含义' + ' 但不能出现直播违禁词包括但不限于（' \
                          f'包含“最”及相关词语,包含“一”及相关词语，包含“级/极”及相关词语，包含“首/家/国”及相关词语，表示权威的禁忌词，' \
                          f'虚假承诺和高风险诱导类的，表示绝对、极限且无法考证的词语，涉迷信宣传的，与欺诈有关 涉嫌欺诈消费者，医疗器械/滋补膳食/保健食品类商品' \
                          f'），要保证每个段落内容丰满。'
        # prompt = f'将以下文本按照{copy_style}进行文本扩展并生成多条不同但类似文本：' + prompt +' 但不能出现直播违禁词包括但不限于（' \
        #                   f'包含“最”及相关词语,包含“一”及相关词语，包含“级/极”及相关词语，包含“首/家/国”及相关词语，表示权威的禁忌词，' \
        #                   f'虚假承诺和高风险诱导类的，表示绝对、极限且无法考证的词语，涉迷信宣传的，与欺诈有关 涉嫌欺诈消费者，医疗器械/滋补膳食/保健食品类商品' \
        #                   f'），要保证每个段落内容丰满。'
        add_txt = ScriptDatum(
            question=title,
            analyzedReply=prompt,
            userId=user_id
        )
        session.add(add_txt)
        session.commit()
        q_id = add_txt.questionId
        reply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
        if "error" in reply:
            return {'message': 'error', 'status': 200, }
        else:
            session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update({'reply': reply})
            session.commit()

        return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': reply}}


def reply_prompt_join(data,user_id):
    crmeb_session = CrmebSession()
    session = Session()
    title = data.get('title')
    q_id = data.get('q_id')
    reply_type = data.get("reply_type")  # 回复类型
    prompt = data.get('prompt')  # 输入
    weijin = ' 但不能出现直播违禁词包括但不限于（' \
                          f'包含“最”及相关词语,包含“一”及相关词语，包含“级/极”及相关词语，包含“首/家/国”及相关词语，表示权威的禁忌词，' \
                          f'虚假承诺和高风险诱导类的，表示绝对、极限且无法考证的词语，涉迷信宣传的，与欺诈有关 涉嫌欺诈消费者，医疗器械/滋补膳食/保健食品类商品' \
                          f'），要保证每个段落内容丰满。'
    ext_type = data.get('ext_type')
    if q_id:
        title, reply = session.query(ScriptDatum.question, ScriptDatum.reply).filter(
            ScriptDatum.questionId == q_id).first()
        prompt = '基于之前对话接着再生成不同的文本'
        print(reply)
        newreply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
        if "error" in newreply:
            return {'message': 'error', 'status': 200, }
        else:
            updated_reply = reply + "\n" + newreply

            # 找到相应的记录并更新reply字段
            session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update({'reply': updated_reply})
            session.commit()
            return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': newreply}}
    else:
        if reply_type == 1:
            prompt = '请将以上产品信息进行{}文本扩展。并生成多条不同类型文本：'.format(ext_type) + prompt + weijin
        elif reply_type == 0:
            prompt = '请将以上信息进行{}文本扩展并生成多条不同类型的文本：'.format(ext_type) + prompt+ weijin
        else:
            prompt = '请将以上地址信息进行{}文本扩展。并生成多条不同类型的文本：'.format(ext_type) + prompt+ weijin
        add_txt = ScriptDatum(
            question=title,
            analyzedReply=prompt,
            userId=user_id
        )
        session.add(add_txt)
        session.commit()
        q_id = add_txt.questionId
        reply = Chat_msg({'prompt': prompt, 'role': title, "convo_id": q_id})  # 请求chat
        if "error" in reply:
            return {'message': 'error', 'status': 200, }
        else:
            session.query(ScriptDatum).filter(ScriptDatum.questionId == q_id).update({'reply': reply})
            session.commit()

    return {'message': 'ok', 'status': 200, 'data': {'id': q_id, 'data': reply}}




def str_fill(prompt,arg,arg_str):
    '''

    :param prompt: prompt语句
    :param arg: 传入的字典或者列表
    :param arg_str: 对应字典的字符串字典
    :return:
    '''
    if isinstance(arg, list):  # 当传入的为列表时
        index = len(arg)  # 记录长度用以循环拼接
        for i in range(index):
            for key in arg[i]:  #  循环提取每一个字典中的key
                if arg[i].get(key):  # 当key存在时
                    print(arg[i].get(key))
                    prompt += arg_str.get(key).format(arg[i].get(key))  # 将对应的字符格式化填充到对应的语句中并拼接到prompt
    else:  # 当直接为字典时
        for key in arg: # 循环提取字典中的key
            if arg.get(key):  # 判断是否存在（写注释的时候发现好像有点子多余，可以删掉吧）
                print(arg.get(key))
                prompt += arg_str.get(key).format(arg.get(key))  # 将对应的字符格式化填充到对应的语句中并拼接到prompt


    return prompt






