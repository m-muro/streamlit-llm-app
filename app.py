import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

# 専門家の定義
EXPERTS = {
    "ソフトウェアエンジニア": "あなたは経験豊富なソフトウェアエンジニアです。プログラミング、システム設計、ベストプラクティスについて専門的なアドバイスを提供してください。",
    "データサイエンティスト": "あなたは熟練したデータサイエンティストです。データ分析、機械学習、統計学について専門的な知見を提供してください。",
    "ビジネスコンサルタント": "あなたは優秀なビジネスコンサルタントです。経営戦略、業務改善、市場分析について専門的なアドバイスを提供してください。"
}

def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    LLMから回答を取得する関数
    
    Args:
        user_input (str): ユーザーの入力テキスト
        expert_type (str): 選択された専門家のタイプ
    
    Returns:
        str: LLMからの回答
    """
    # ChatOpenAIのインスタンスを作成
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # システムメッセージを取得
    system_message = SystemMessage(content=EXPERTS[expert_type])
    human_message = HumanMessage(content=user_input)
    
    # LLMに問い合わせ
    response = llm.invoke([system_message, human_message])
    
    return response.content

# Streamlitアプリのメイン部分
def main():
    st.title("🤖 AI専門家チャット")
    
    # アプリの概要
    st.markdown("""
    ## 📖 概要
    このアプリでは、様々な分野の専門家としてAIに質問することができます。
    
    ## 🎯 使い方
    1. **専門家を選択**: ラジオボタンから相談したい専門家のタイプを選択してください
    2. **質問を入力**: テキストエリアに質問や相談内容を入力してください
    3. **送信**: 「回答を取得」ボタンをクリックすると、選択した専門家の視点で回答が表示されます
    """)
    
    st.divider()
    
    # 専門家の選択
    st.subheader("👤 専門家を選択")
    expert_type = st.radio(
        "どの分野の専門家に相談しますか？",
        options=list(EXPERTS.keys()),
        index=0
    )
    
    # 選択された専門家の説明を表示
    st.info(f"**選択中**: {expert_type}\n\n{EXPERTS[expert_type]}")
    
    # 入力フォーム
    st.subheader("💬 質問を入力")
    user_input = st.text_area(
        "質問や相談内容を入力してください",
        height=150,
        placeholder="例: Pythonでデータ分析を始めるには何から学べばいいですか？"
    )
    
    # 送信ボタン
    if st.button("🚀 回答を取得", type="primary"):
        if user_input.strip():
            with st.spinner("回答を生成中..."):
                try:
                    # LLMから回答を取得
                    response = get_llm_response(user_input, expert_type)
                    
                    # 回答を表示
                    st.subheader("✨ 回答")
                    st.success(response)
                    
                except Exception as e:
                    st.error(f"エラーが発生しました: {str(e)}")
        else:
            st.warning("質問を入力してください。")

if __name__ == "__main__":
    main()