from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# main.py
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
import streamlit as st

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL="gpt-4-0125-preview"

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

want_to = """너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
content
{}
"""

content="""
드록바는 첼시 역사상 최고의 스트라이커로 꼽히는 살아있는 전설입니다. 위상으로 따지면 아스널의 앙리가 대접받는 것과 같을 정도로 엄청난 선수입니다.
특히 현재 첼시는 드록바 같은 선수를 원할 정도로 엄청난 스트라이커였고, 아프리카 역대 최고의 선수입니다.2004-05 시즌 드록바는 첼시에 입단했습니다.
2004-05시즌에는 10골로 데뷔 시즌 치고는 나쁘지 않은 성적이었습니다. 주전급으로 활약하고 있었다 하지만 EPL 진출 초기의 드록바는 다이빙의 대명사였습니다. 
드록바의 다이빙을 비꼬는 맥주 CF까지 등장할 정도로 드록바의 할리우드 액션은 수많은 이들의 비난을 받았습니다.
이러한 지저분한 플레이 스타일과 더불어 득점 개수도 그다지 높지 않았던 데다 득점 장면도 왠지 억지로 밀어 넣는 듯한 장면이 많이 연출되면서 뽀록바라 불리며 엄청나게 까였습니다.
2005-06 시즌 드록바는 EPL에 점점 적응해가며 주전을 더욱 굳혀갔습니다.
드록바는 발전된 골 결정력으로 짧은 시간 내 첼시의 없어서는 안 될 공격 자원으로 등극하였으며, 05/06 시즌에는 11개의 어시스트를 기록하면서 프리미어리그 도움왕에 올랐습니다.
2006-07 시즌 드록바는 등번호를 15에서 11번으로 바꿨고 이는 첼시에 뛰는 동안 계속 유지되었습니다.
시즌 시작 전, 안드리 셰브첸코의 영입으로 드록바의 자리는 사라진다는 조롱 섞인 기사들이 타블로이드지를 장식하기 시작했습니다.
그러나 맨체스터 시티와의 개막전에서 마수걸이 골을 성공시킨 이후, 리버풀, 바르셀로나와 같은 강팀들을 상대로도 어렵지 않게 골을 뽑아내며,
지고 있는 상황에서도 기어코 역전승을 만들어내는 커리어 사상 최고의 시즌을 보내게 되었습니다.
이 시즌의 활약으로 FIFA FIFPRO 월드 XI, UEFA 올해의 팀에 포함되었으며, 드록신이라는 별명도 이때 만들어졌습니다.
리그 우승에는 비록 실패했지만 2007년 프리미어리그에서 20골을 넣으며 아프리카인 최초로 득점왕에 올랐습니다.
2007-08 시즌 부상과 부진 등으로 아쉬운 활약을 펼쳤습니다. 그러나 챔피언스리그 최고의 모습을 보이기도 했습니다.
모스크바에서 펼쳐진 맨유와의 결승전에서 결승전에선 골대를 맞추는 등 분전했다만 연장 후반 막판 비디치의 뺨을 때리고 퇴장당하여 첼시의 첫 번째 챔스 우승 도전이 실패하는 한 원인이 되기도 하였습니다.
2008-09 시즌 팀의 주포로서 제대로 된 활약을 하지 못하고 부상과 징계와 함께 니콜라 아넬카에게 원톱 자리를 내주고 방황하고 말았습니다.
팀의 주포로서 제대로 된 활약을 하지 못하고 부상과 징계와 함께 니콜라 아넬카에게 원톱 자리를 내주고 방황하고 말았습니다.
그래도 다행히 히딩크 부임 후로 점차 나아졌습니다. 특히 챔피언스리그에서는 16강 유벤투스 전부터 8강 리버풀전까지 4경기에서 모두 득점을 기록하면서 준결승 진출에 기여했습니다.
2009-10 시즌 전성기 시작했습니다.개막전에서 헐시티를 상대로 프리킥으로 동점골을 만든 뒤 후반 추가시간에 데쿠의 패스를 받아 왼쪽 측면에서 절묘한 칩슛으로 역전골을 만들어 극적인 2 대 1 승리를 이끌었습니다.
7 라운드 위건 원정에서는 동점골로 시즌 6호 득점을 성공시켰으나 3 대 1 패배를 막지 못했습니다. 이 골은 자신의 첼시 100호 득점이었습니다.
안첼로티 감독 부임 이후 리그에서 웨인 루니의 부상을 틈타 29골 10도움의 눈부신 활약으로 인해 다시금 드록신이 되었으며, 득점왕까지 차지했습니다.
어시스트도 리그 3위에 해당하는 기록이었습니다. 29골 중 페널티로 얻은 득점은 마지막 위건전에서 1골뿐이며 나머지가 전부 필드골인 점도 대단했습니다.
챔스는 비록 인테르에 밀려 16강에서 탈락하나 리그에서는 최강의 모습이었습니다.
팀은 결국 리그 우승을 차지했으며 FA컵까지 제패하며 창단 첫 더블을 달성하였습니다.
2010-11 시즌 프리미어리그 7라운드 기준 6골 7도움으로 득점, 어시스트 모두 공동 1위를 달렸습니다. 그러나 그 이후 폼이 급격히 떨어지며 꽤 긴 부진에 빠졌습니다.
1월 25일 볼턴 원더러스 전에서 패스 미스로 흘러나온 공을 받자마자 거의 하프라인 가까운 지점에서 중거리 슈팅, 그대로 선제골을 기록했습니다.
이 슛은 무회전이 걸려 뚝 떨어지면서도 좌우 지그재그로 흔들리는 궤도를 탔습니다.
이후 4월 13일 맨체스터 유나이티드와의 10/11 UEFA 챔피언스리그 8강 2차전에서 하프타임에서 페르난도 토레스와 교체 출장을 했습니다.
0 대 1로 뒤진 후반 하미레스가 경고 누적으로 퇴장당한 상황에서 추격에 불을 지피는 동점골을 집어넣으며 오랜만에 드록신으로 재림하나 싶었으나,
곧바로 박지성에게 1분 만에 골을 먹으면서 결국 이날의 활약은 없었던 것이 되어버렸습니다.
그리고 5월 9일 사실상 리그 우승의 향방이 갈리던 맨체스터 유나이티드와의 경기에서 결국 챔피언스리그에 이어 또다시 패배하며 리그 우승마저 넘겨줬습니다.
2011-12 시즌 전성기급의 활약을 보여줬습니다.
3라운드 노리치 전에서 후반 골키퍼와 경합 도중 골키퍼의 펀칭을 그대로 얻어맞아 공중에서 기절하고 떨어졌습니다.
경추골절이라는 말까지 나왔으나 다행히도 첼시 공홈에서 경미한 뇌진탕이라고 발표가 나왔습니다.
12월 7일에 벌어진 챔피언스리그 조예선 6차전 발렌시아전에서 2골 1도움을 기록하며 첼시의 3 대 0 승리의 일등공신이 됐습니다.
5월 9일 리버풀과의 FA컵 결승에서 1 대 0으로 앞서고 있던 후반 6분에 추가골을 넣었고, 최종 스코어 2 대 1로 드록바의 골이 결승골이 되었습니다.
5월 19일 열린 챔피언스리그 결승 바이에른 뮌헨전이 뭰헨 홈구장 알리안츠 아레나에서 열렸습니다.
팀이 후반전 토마스 뮐러에게 골을 먹혀 지고있던 상황에서 드록바는 극적인 동점골을 넣어 승부차기까지 경기를 끌고 갔습니다. 
그리고 승부차기에서도 마지막 키커로 골을 넣어 4 대 3으로 첼시의 사상 첫 챔피언스리그 우승이자 자신의 클럽축구 인생 최대 우승의 영광을 맛보았습니다.
그리고 이후 5월 22일, 새로운 도전을 위해 첼시를 떠나는 게 확정됐습니다.
"""
st.header("최고의 ST")
st.info("첼시 공격수 드록바에 대한 정보를 알려주는 Q&A 로봇입니다.")
st.error("내가 하고 싶은거 할래")

if "messages" not in st.session_state:
    st.session_state["messages"] = [ChatMessage(role="assistant", content="안녕하세요! 백엔드 스쿨 Q&A 로봇입니다. 어떤 내용이 궁금하신가요?")]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    if not API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(openai_api_key=API_KEY, streaming=True, callbacks=[stream_handler], model_name=MODEL)
        response = llm([ ChatMessage(role="system", content=want_to.format(content))]+st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))