 Создать сериалайзер для модели User.
 Реализовать вьюхи (наследуясь от APIView)
    для получения списка категорий/постов (метод get),
    создания категорий/постов (метод post),
    частичного обновления постов (метод patch)
    и удаления постов (метод delete).

По поводу проблемы с категориями:
не используйте вложенный сериалайзер для категорий.
Поле категории в сериалайзере поста
должно принимать id категории (IntegerField)
