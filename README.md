# 🤖 AI専門家チャットアプリ

StreamlitとLangChainを使用した、AI専門家に質問できるWebアプリケーションです。

## 📋 機能

- **3つの専門家タイプ**: ソフトウェアエンジニア、データサイエンティスト、ビジネスコンサルタントから選択
- **対話型インターフェース**: シンプルで使いやすいUI
- **LangChain統合**: OpenAI GPTモデルを使用した高品質な回答生成

## 🚀 セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env`ファイルを作成し、OpenAI APIキーを設定してください：

```bash
cp .env.example .env
```

`.env`ファイルを編集：

```
OPENAI_API_KEY=your-actual-api-key-here
```

### 3. アプリの起動

```bash
streamlit run app.py
```

## 💡 使い方

1. ラジオボタンから相談したい専門家のタイプを選択
2. テキストエリアに質問や相談内容を入力
3. 「回答を取得」ボタンをクリック
4. AI専門家からの回答が表示されます

## 🛠️ 技術スタック

- **Streamlit**: Webアプリフレームワーク
- **LangChain**: LLMアプリケーション構築フレームワーク
- **OpenAI GPT**: 言語モデル
- **Python-dotenv**: 環境変数管理

## 📝 注意事項

- OpenAI APIキーが必要です
- APIの使用には料金が発生する場合があります