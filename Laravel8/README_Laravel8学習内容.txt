ツール：Docker Desktop, VS Code, Edge Browser, Windows11

基本機能編：
開発の大きな流れを理解する。
web.php にルーティングを定義して、対応する処理は Controller に書く。Controller の処理では、 view を呼び出しページを表示させる。
viewでは、コンポーネントを活用し、 Controller から渡された値を埋め込む。

データベース編：
Laravelとデータベースを連携させる。
CRUDのReadを行い、データの表示処理をする。
投稿の一覧ページと詳細ページをデータベースを使って実装する。

CRUD処理編：
CRUD機能を持つアプリケーションを構築する。
CRUDのUpdateとDeleteを行い、投稿を追加・削除をする。

リレーション編：
モデル間にリレーションを設定する。
CRUD処理編までに作成した掲示板に、コメント機能を実装する。


＃Dotinstallより

Basic Functionality:
Understanding the main development flow:
Define routes in web.php and associate them with corresponding actions in controllers. In the controllers, call views to display pages. Utilize components in views to embed values passed from the controller.

Database Integration:
Connect Laravel with the database.
Perform CRUD's Read operation to display data.
Implement the list page and detail page of posts using the database.

CRUD Operations:
Build an application with CRUD functionalities.
Perform CRUD's Update and Delete operations to add and delete posts.

Relation:
Set up relations between models.
Implement a comment feature in the bulletin board created in the CRUD Operations section.