# React コンポーネント・状態管理

- [React の部品の組み立て方](react-component-composition.md) - React でコンポーネントにデータを渡して組み立てる方法（props の読み方・既定値・転送、children での JSX の受け渡し、props の不変性、prop drilling と Context の使い分け、Context の作り方・使い方・提供の仕方と使いどころ）。
- [React カスタムフックの責務分離とライフサイクル設計指針](react-hook-separation-and-lifecycle.md) - React カスタムフックで状態とロジックを分離し、ライフサイクルを設計する指針。
- [React の state の持ち主とデータの流れ](react-state-ownership.md) - React で state をどのコンポーネントが持ち、データをどう流すかを決める考え方（UI の分け方、最小の state、共通の親への持ち上げ、制御されたコンポーネント、一方向のデータフロー）。
- [React の画面の切り替えと state のリセット](react-state-reset-by-position.md) - React の state がツリー上の位置で管理されることを使い、画面を切り替えたときに state を作り直す設計の指針。
- [React の state の持ち方](react-state-structure.md) - React の state を設計するときの原則と、state を Effect で導出・同期しない考え方（関連する state のまとめ方、矛盾・冗長・重複・深い入れ子の避け方、描画中の計算、key によるリセット）。
