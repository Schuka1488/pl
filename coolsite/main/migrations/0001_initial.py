# Generated by Django 4.2.7 on 2023-11-27 14:05

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginAccount', models.CharField(default='', max_length=60, verbose_name='Логин')),
                ('passwordAccount', models.CharField(default='', max_length=60, verbose_name='Пароль')),
                ('roleTitleAccount', models.CharField(default='', max_length=50, verbose_name='Название роли')),
                ('idNameInGameAccount', models.CharField(default='', max_length=100, verbose_name='ID игрока (ник в игре)')),
                ('emailBuyerAccount', models.CharField(blank=True, default='', max_length=150, verbose_name='Email игрока')),
                ('onlineStatusAccount', models.BooleanField(default=True, verbose_name='Статус нахождения в сети')),
                ('authorizationStatusAccount', models.BooleanField(default=False, verbose_name='Статус авторизации пользователя на сайте')),
                ('serverPlayerAccount', models.CharField(blank=True, default='', max_length=50, verbose_name='Игровой сервер')),
            ],
            options={
                'verbose_name': 'Аккаунты',
                'verbose_name_plural': 'Аккаунты',
            },
            managers=[
                ('objectsAccount', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(db_index=True, default='', max_length=200, verbose_name='Название категории')),
                ('slugCategory', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
            managers=[
                ('objectsCategory', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOrder', models.IntegerField(default=0, verbose_name='Номер заказа')),
                ('sellProductOrder', models.CharField(default='', max_length=250, verbose_name='Проданные товары')),
                ('statusSellOrder', models.BooleanField(default=False, verbose_name='Статус выполнения заказа')),
                ('dateSellProductOrder', models.DateTimeField(auto_now_add=True, max_length=75, verbose_name='Дата выполнения заказа')),
                ('loginOrder', models.CharField(default='', max_length=60, verbose_name='Логин заказчика')),
                ('idPlayerOrder', models.CharField(default='', max_length=100, verbose_name='ID игрока (ник в игре)')),
                ('emailBuyerOrder', models.CharField(blank=True, default='', max_length=150, verbose_name='Email игрока')),
                ('paymentGatewayOrder', models.CharField(default='', max_length=100, verbose_name='Выбранный платежный шлюз')),
                ('countSameTypeOrder', models.IntegerField(blank=True, default=0, verbose_name='Количество проданных товаров одного типа')),
                ('countDifferentTypeOrder', models.IntegerField(blank=True, default=0, verbose_name='Количество проданных товаров разного типа')),
                ('playServerOrder', models.CharField(default='', max_length=50, verbose_name='Игровой сервер')),
                ('orderPriceRememberOrder', models.IntegerField(default=0, verbose_name='Цена заказа')),
                ('statusReadyAgreementPurchaseOfGood', models.BooleanField(default=False, verbose_name='Статус подтверждения ПС')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
            managers=[
                ('objectsOrder', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starReview', models.IntegerField(default=0, verbose_name='Количество звезд')),
                ('textReview', models.CharField(blank=True, default='', max_length=500, verbose_name='Текст отзыва')),
                ('nameReview', models.CharField(default='', max_length=50, verbose_name='Имя клиента')),
                ('emailBuyerAccount', models.CharField(default='', max_length=150, verbose_name='Email клиента')),
                ('answerReview', models.CharField(blank=True, default='', max_length=500, verbose_name='Ответ на отзыв')),
                ('statusViewsOnSiteReview', models.BooleanField(default=True, verbose_name='Статус отображения на сайте')),
                ('dateReview', models.DateTimeField(auto_now_add=True, max_length=75, verbose_name='Дата написания отзыва')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(default='', max_length=150, verbose_name='Название продукта')),
                ('photoProduct', models.ImageField(blank=True, default='', upload_to='photos/photoProduct/nameProduct', verbose_name='Фото товара')),
                ('priceOnCronOrNotProduct', models.BooleanField(default=True, verbose_name='В кронах ли цена?')),
                ('priceOnCronProduct', models.IntegerField(blank=True, default=0, verbose_name='Цена в игровой валюте (кроны или гемы)')),
                ('priceOnMoneyProduct', models.IntegerField(default=0, verbose_name='Цена в реальной валюте')),
                ('descriptionProduct', models.CharField(blank=True, default='', max_length=200, verbose_name='Описание товара')),
                ('statusViewsOnSiteProduct', models.BooleanField(default=True, verbose_name='Статус отображения на сайте')),
                ('promotionStatusProduct', models.BooleanField(default=False, verbose_name='Статус акции у товара')),
                ('slugProduct', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
            managers=[
                ('objectsProduct', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateWriteChat', models.DateTimeField(auto_now_add=True, max_length=75, verbose_name='Дата написания сообщения')),
                ('textReview', models.CharField(default='', max_length=500, verbose_name='Текст сообщения')),
                ('statusViewsOnSiteChat', models.BooleanField(default=True, verbose_name='Статус отображения на сайте')),
                ('loginAccountChat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.account')),
            ],
            options={
                'verbose_name': 'Сообщения в чате',
                'verbose_name_plural': 'Сообщения в чате',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='idNumberOrder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.order'),
        ),
    ]
