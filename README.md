### Debank Hisotry CSV君 ###
Wallet関連で税金計算に困っている方は多いと思います。
Cryptactとかにぶっこむ前に、整理されたTXのリストがCSVとかでほしくないですか？！？！？
特にEth以外のEVM系のマイナーチェーン！！！

そこでDebankのHistory機能が割と良さそうだと思ったので見てみるがHistoryをCSVにする機能がない！！！
ということでDebankのHistoryをCSVに落とす機能を作りました。（かなり雑）

## 使い方 ##
①DebankのHistoryページへGo!

②Historyを全部読み込む（ひたすら下スクロール）

③F12を押して開発者ツールを出す
![image](https://user-images.githubusercontent.com/79858324/150699342-7bfc37c3-cf4a-4ff9-b0c2-9ada08ea8455.png)

④HistoryのTableのHTMLをコピー（対象Tableを右クリック->Copy->Copy Element)

⑤コピーしたやつをPythonのmain.pyにコピペしてRun
main.py -> text = 'ここにDebankのHistoryのテーブルいれる'

⑥ConsoleにCSVを意識したTextが張り出されるから、Textファイルにコピペして、拡張子をcsvに

こんなかんじのやつできる
![image](https://user-images.githubusercontent.com/79858324/150699413-e9d9c296-4f24-4b5a-840a-1bda705ddcf1.png)

## 注意事項 ##
かなり雑なコードなので誰か整形してください
何故か1行目がばぐったりします
BSC, MaticなどではNFTが反映されていないためそこは手動での対応が必要そうです。
Ethも最終的な枚数と合わなかったので、こちらも参考程度にするのがよいかもしれません（Zerionのほうがいいかも）
