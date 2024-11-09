from fastapi import APIRouter,Depends
from typing import Dict
import sqlalchemy
from sqlalchemy import desc
from app.db.dataBase import Session
from app.db.model.SpeechScript import SpeechScript
from app.db.model.ScriptDatum import ScriptDatum
from app.util.TokenUtil import get_user_id
from app.util.TokenUtil import get_id
from app.util.dataModel import Audio_list
from app.util.dataModel import Chat_replymeg



router = APIRouter(prefix="/audio_list", tags=["音色"])



@router.post("", summary="audio_list")
async def audio_list(item: Audio_list, user_id_data: int = Depends(get_id)):
    result = {'data': []}
    session =Session()
    try:
        bu'f' = item
        # user_query = data.get('user_query')
        # user_id = data.get('user_id')
        page = data.page
        page_size = data.page_size
        offset = (page - 1) * page_size

        user_id = user_id_data
        print(user_id)
        # query = session.query(tone)
        # ession.query(SpeechScript).filter_by(userId=user_id, isDeleted=0).group_by(SpeechScript.title).order_by(SpeechScript.textId).desc()
        total = session.query(SpeechScript).filter_by(userId=user_id, isDeleted=0).group_by(SpeechScript.title).count()
        # 查询指定用户ID的所有数据，并按问题ID排序
        title_list = session.query(SpeechScript.title).filter_by(userId=user_id, isDeleted=0).group_by(
            SpeechScript.title).order_by(desc(SpeechScript.textId)).offset(offset).limit(page_size).all()
        query_results = session.query(SpeechScript).filter(SpeechScript.userId == user_id, SpeechScript.isDeleted == 0)

        # 遍历查询结果
        for title in title_list:
            id = int(title[0])
            # print(id)
            script_data = session.query(ScriptDatum).filter(ScriptDatum.questionId == id).first()
            # 创建新的 message 结构并加入到结果列表中
            # print(title)
            current_question_group = {
                'title': script_data.question,
                'updatatime': script_data.updateTime,
                'data': []
            }
            result['data'].append(current_question_group)
            title_data = query_results.filter(SpeechScript.title == title[0]).all()
            for item in title_data:
                # 将当前项目添加到当前问题ID的分组中
                current_question_group['data'].append({
                    'text': item.scriptText,
                    'audioUrl': item.audioUrl,
                    'role': item.txt_role,
                    'id': item.textId,
                    'consumption': item.consumption,
                    'residual': item.residual
                })
        # 将结果转换为JSON
        # print(result)
        result['status'] = 200
        result['message'] = 'ok'
        result['page'] = page
        result['page_size'] = page_size
        result['total'] = total
        # result['consumption']=consumption
        # json_result = jsonify(result)

        return result
    except Exception as e:
        print(str(e))
        return {'message': 'error', 'status': 10000}
    finally:
        session.close()