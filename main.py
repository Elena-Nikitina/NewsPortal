# Список команд, запускаемых в Django shell:
# 1.	Создать двух пользователей
# U1 = User.objects.create_user(username='Alex')
# U2 = User.objects.create_user(username='Nikita')
# U3 =  User.objects.create_user(username='Bill')
# U4 =  User.objects.create_user(username='Kate')
#
# 2.	Создать объекты модели Author, связанные с пользователями.
# Author.objects.create(authorUser=U1)
# Author.objects.create(authorUser=U3)
# Author.objects.create(authorUser=U4)
# 3.	Добавить 4 категории в модель Category.
# Category.objects.create(name='IT')
# Category.objects.create(name='Art')
# Category.objects.create(name='Fashion')
# Category.objects.create(name='Tech')
# 4.	Добавить статьи и новости.
# author = Author.objects.get(id=1)
# author2 = Author.objects.get(id=2)
# Post.objects.create(author=author, categoryType='NW', title='sometitle', text='bigtext')
# Post.objects.create(author=author, categoryType='AR', title='sometitle', text='bigtext')
# Post.objects.create(author=author, categoryType='AR', title='sometitle', text='bigtext')
# Post.objects.create(author=author2, categoryType='NW', title='sometitle', text='bigtext')
# Post.objects.create(author=author2, categoryType='AR', title='sometitle', text='bigtext')
# 5.	Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))
# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
# Post.objects.get(id=4).postCategory.add(Category.objects.get(id=3))
# Post.objects.get(id=5).postCategory.add(Category.objects.get(id=2))
# 6.	Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')
# Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')
# Comment.objects.create(commentPost=Post.objects.get(id=5), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')
# 7.	Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=1).dislike()
# Comment.objects.get(id=1).dislike()
# Comment.objects.get(id=1).dislike()
# Comment.objects.get(id=1).rating
#
# Comment.objects.get(id=2).dislike()
# Comment.objects.get(id=2).like()
# Comment.objects.get(id=2).like()
# Comment.objects.get(id=2).rating
#
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=3).dislike()
# Comment.objects.get(id=3).rating
#
# Comment.objects.get(id=4).like()
# Comment.objects.get(id=4).like()
# Comment.objects.get(id=4).like()
# Comment.objects.get(id=4).like()
# Comment.objects.get(id=4).rating
# Comment.objects.get(id=5).like()
# Comment.objects.get(id=5).like()
# Comment.objects.get(id=5).dislike()
# Comment.objects.get(id=5).dislike()
# Comment.objects.get(id=5).dislike()
# Comment.objects.get(id=5).rating
#
# Comment.objects.get(id=6).like()
# Comment.objects.get(id=6).like()
# Comment.objects.get(id=6).dislike()
# Comment.objects.get(id=6).rating
#
# Post.objects.get(id=1).like()
# Post.objects.get(id=2).like()
# Post.objects.get(id=3).like()
# Post.objects.get(id=3).dislike()
# Post.objects.get(id=4).like()
# Post.objects.get(id=4).like()
# Post.objects.get(id=4).rating
#
# Post.objects.get(id=5).like()
# Post.objects.get(id=5).like()
# Post.objects.get(id=5).dislike()
# Post.objects.get(id=5).rating
# 8.	Обновить рейтинги пользователей.
# a = Author.objects.get(id=1)
# a.update_rating()
# a.ratingAuthor
# b = Author.objects.get(id=2)
# b.update_rating()
# b.ratingAuthor
# 9.	Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# a = Author.objects.order_by('-ratingAuthor')[:1]
# for i in a:
#     i.ratingAuthor
#     i.authorUser.username
# 10.	Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# b = Post.objects.order_by('-rating')[:1].values('author', 'dateCreation', 'rating', 'title', 'text')
# for i in b:
#     i.author
#     i.dateCreation
#     i.rating
#     i.title
#     i.text

# Author.objects.get(pk=2).authorUser
# b = Post.objects.order_by('-rating')[0]
# b.preview()
# 11.	Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
# Comment.objects.filter(commentPost=4).values('commentUser', 'dateCreation', 'text', 'rating')









