Задание 2. https://docs.google.com/spreadsheets/d/1a9s0XqmqUGzi-wcK9_Agj2vjC6H6P_uDhhKVS8cOW0A/edit?usp=sharing - чек лист тестирования телеграм-бота для конвертации валют. Имя в телеграме @QAP_Convertbot

Задание 1.
# QAP-1037-Module-18-crypto_bot
Имя в телеграме @aliceunfibot

Ваше задание: написать и протестировать Telegram-бота, в котором будет реализован следующий функционал:

Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
При написании бота необходимо использовать библиотеку pytelegrambotapi.
Человек должен отправить сообщение боту в виде <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.
При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
Для взятия курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
Для парсинга полученных ответов использовать библиотеку JSON.
При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента: имя валюты, цену на которую надо узнать, — base, имя валюты, цену в которой надо узнать, — quote, количество переводимой валюты — amount и возвращает нужную сумму в валюте.
Токен telegramm-бота хранить в специальном конфиге (можно использовать .py файл).
Все классы спрятать в файле extensions.py.
