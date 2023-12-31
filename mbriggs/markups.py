from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline():
    buttons = [
        [
            InlineKeyboardButton(text="a", callback_data="a"),
            InlineKeyboardButton(text="b", callback_data="b"),
        ],
        [
            InlineKeyboardButton(text="⏮", callback_data="⏮"),
            InlineKeyboardButton(text="⏭", callback_data="⏭"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


start = """
Привет! Это бот <b>АрхиПрофессионал</b>.
Смотри, что я могу!

Личностный тест Майерс-Бриггс:
Все подробности о тесте по команде ниже. Скорее нажимай!
<b>/mbriggs_test - Пройти тест</b>

Закладки:
В закладку можете добавить любое сообщение, отправленное боту (фото, видео, музыку и т.д.).
Если не хотите переписывать чужое сообщение, то просто перешлите его 😉
Для закладки нужно будет название, которое Вам поможет запомнить, что находить в сообщении.
Список названий будет в /list. При нажатии, текст скопируется!
<b>/add - Добавить сообщение в закладки
/get - Показать сообщение из закладок

</b>Выход:
Из теста или любого действия с закладками можно просто выйти по команде ниже.<b>
/cancel - Отмена действия
</b>
"""
####################################ОПРОС########################################
text1 = """Это Тест 8. Инструкция к тесту: Этот вопросник предназначен для определения типичных способов поведения и личностных характеристик. Он состоит из 70 утверждений (вопросов), каждое из которых имеет два варианта ответа. Вам необходимо выбрать ОДИН. Все ответы равноценны, среди них нет "правильных" или "неправильных"! Поэтому не нужно "угадывать" ответ. Выберите ответ, который свойствен вашему поведению в большинстве жизненных ситуаций. Работайте последовательно, не пропуская вопросов. Отвечайте правдиво, если вы хотите узнать что-то о себе, а не о какой-то мифической личности.

<i>На каждый вопрос можно ответить повторно! Вопросы, на которые Вы ответили будут с указанием ответа ниже вопроса!
Переходить на следующий вопрос можно только, если ответили на предыдущие!
</i>
        """

# start
name = """
Введите ваше имя:
"""

email = """
Введите ваш email:
"""

mob_tel = "Введите ваш номер телефона(только цифры, без пробелов и спец. символов):"

ready = """Начнём? Ответьте на 70 вопросов, обычно это занимает 3-5 минут    .
"""

user_naber_1 = "1. В компании (на вечеринке) Вы \nа) общаетесь со многими, включая и незнакомцев; \nб) общаетесь с немногими - Вашими знакомыми. "
user_naber_2 = "2. Вы человек скорее \nа) реалистичный, чем склонный теоретизировать; \nб) склонный теоретизировать, чем реалистичный. "
user_naber_3 = "3. По-вашему, что хуже: \nа) витать в облаках; \nб) придерживаться проторенной дорожки. "
user_naber_4 = (
    "4. Вы более подвержены влиянию \nа) принципов, законов; \nб) эмоций, чувств. "
)
user_naber_5 = "5. Вы более склонны \nа) убеждать; \nб) затрагивать чувства."
user_naber_6 = "6. Вы предпочитаете работать \nа) выполняя все точно в срок; \nб) не связывая себя определенными сроками. "
user_naber_7 = (
    "7. Вы склонны делать выбор \nа) довольно осторожно; \nб) внезапно, импульсивно."
)
user_naber_8 = "8. В компании (на вечеринке) Вы \nа) остаетесь допоздна, не чувствуя усталости; \nб) быстро утомляетесь и предпочитаете пораньше уйти."
user_naber_9 = "9. Вас более привлекают \nа) здравомыслящие люди; \nб) люди с богатым воображением. "
user_naber_10 = "10. Вам интересно \nа) то, что происходит в действительности; \nб) те события, которые могут произойти."
user_naber_11 = "11. Оценивая поступки людей, Вы больше учитываете \nа) требования закона, чем обстоятельства; \nб) обстоятельства, чем требования закона. "
user_naber_12 = "12. Обращаясь к другим, Вы склонны \nа) соблюдать формальности, этикет; \nб) проявлять свои личные, индивидуальные качества. "
user_naber_13 = (
    "13. Вы человек скорее \nа) точный, пунктуальный; \nб) неторопливый, медлительный."
)
user_naber_14 = "14. Вас больше беспокоит необходимость \nа) оставлять дела незаконченными; \nб) непременно доводить дела до конца. "
user_naber_15 = "15. В кругу знакомых Вы, как правило \nа) в курсе происходящих событий; \nб) узнаете о новостях с опозданием."
user_naber_16 = "16. Повседневные дела Вам нравится делать \nа) общепринятым способом; \nб) своим оригинальным способом."
user_naber_17 = "17. Предпочитаю таких писателей, которые \nа) выражаются буквально, напрямую; \nб) пользуются аналогиями, иносказаниями. "
user_naber_18 = "18. Что Вас больше привлекает \nа) стройность мысли; \nб) гармония человеческих отношений. "
user_naber_19 = "19. Вы чувствуете себя увереннее \nа) в логических умозаключениях; \nб) в практических оценках ситуаций. "
user_naber_20 = "20. Вы предпочитаете, когда дела \nа) решены и устроены; \nб) не решены и пока не улажены."
user_naber_21 = "21. Как по-вашему, Вы человек, скорее \nа) серьезный, определенный; \nб) беззаботный, беспечный. "
user_naber_22 = "22. При телефонных разговорах Вы \nа) заранее не продумываете все, что нужно сказать; \nб) мысленно репетируете то, что будет сказано. "
user_naber_23 = "23. Как Вы считаете, факты \nа) важны сами по себе; \nб) есть проявления общих закономерностей. "
user_naber_24 = "24. Фантазеры, мечтатели обычно \nа) раздражают Вас; \nб) довольно симпатичны Вам. "
user_naber_25 = (
    "25. Вы чаще действуете как человек \nа) хладнокровный; \nб) вспыльчивый, горячий. "
)
user_naber_26 = "26. Как по-вашему, хуже быть \nа) несправедливым; \nб) беспощадным. "
user_naber_27 = "27. Обычно Вы предпочитаете действовать \nа) тщательно взвесив все возможности; \nб) полагаясь на волю случая. "
user_naber_28 = (
    "28. Вам приятнее \nа) покупать что-нибудь; \nб) иметь возможность купить. "
)
user_naber_29 = "29. В компании Вы, как правило \nа) первым заводите беседу; \nб) ждете, когда с Вами заговорят. "
user_naber_30 = "30. Здравый смысл \nа) редко ошибается; \nб) часто попадает впросак. "
user_naber_31 = "31. Детям часто не хватает \nа) практичности; \nб) воображения. "
user_naber_32 = "32. В принятии решений Вы руководствуетесь скорее \nа) принятыми нормами; \nб) своими чувствами, ощущениями. "
user_naber_33 = (
    "33. Вы человек скорее \nа) твердый, чем мягкий; \nб) мягкий, чем твердый."
)
user_naber_34 = "34. Что, по-вашему, больше впечатляет \nа) умение методично организовать; \nб) умение приспособиться и довольствоваться достигнутым."
user_naber_35 = "35. Вы больше цените \nа) определенность, законченность; \nб) открытость, многовариантность. "
user_naber_36 = "36. Новые и нестандартные отношения с людьми \nа) стимулируют, придают Вам энергии; б} утомляют Вас. "
user_naber_37 = "37. Вы чаще действуете как \nа) человек практического склада; \nб) человек оригинальный, необычный. "
user_naber_38 = "38. Вы более склонны \nа) находить пользу в отношениях с людьми; \nб) понимать мысли и чувства других. "
user_naber_39 = "39. Что приносит Вам больше удовлетворения \nа) тщательное и всесторонне обсуждение спорного вопроса; \nб) достижение соглашения по поводу спорного вопроса. "
user_naber_40 = "40. Вы руководствуетесь более \nа) рассудком; \nб) велениями сердца. "
user_naber_41 = "41. Вам удобнее выполнять работу \nа) по предварительной договоренности; \nб) которая подвернулась случайно. "
user_naber_42 = "42. Вы обычно полагаетесь \nа) на организованность, порядок; \nб) на случайность, неожиданность. "
user_naber_43 = "43. Вы предпочитаете иметь \nа) много друзей на непродолжительный срок; \nб) несколько старых друзей. "
user_naber_44 = "44. Вы руководствуетесь в большей степени \nа) фактами, обстоятельствами; \nб) общими положениями, принципами. "
user_naber_45 = "45. Вас больше интересуют \nа) производство и сбыт продукции; \nб) проектирование и исследования. "
user_naber_46 = "46. Что Вы считаете за комплимент \nа) *Вот очень логичный человек*; \nб) *Вот тонко чувствующий человек*. "
user_naber_47 = "47. Вы более цените в себе \nа) невозмутимость; \nб) увлеченность. "
user_naber_48 = "48. Вы предпочитаете высказывать \nа) окончательные и определенные утверждения; \nб) предварительные и неоднозначные утверждения. "
user_naber_49 = "49. Вы лучше чувствуете себя \nа) после принятия решения; \nб) не ограничивая себя решениями. "
user_naber_50 = "50. Общаясь с незнакомыми, Вы \nа) легко завязываете продолжительные беседы; \nб) не всегда находите общие темы для разговора."
user_naber_51 = "51. Вы больше доверяете \nа) своему опыту; \nб) своим предчувствиям. "
user_naber_52 = "52. Вы чувствуете себя человеком \nа) более практичным, чем изобретательным; \nб) более изобретательным, чем практичным. "
user_naber_53 = "53. Кто заслуживает большего одобрения - \nа) рассудительный, здравомыслящий человек; \nб) человек, глубоко переживающий. "
user_naber_54 = "54. Вы более склонны \nа) быть прямым и беспристрастным; \nб) сочувствовать людям. "
user_naber_55 = "55. Что, по-вашему, предпочтительней \nа) удостовериться, что все подготовлено и улажено; \nб) предоставить событиям идти своим чередом."
user_naber_56 = "56. Отношения между людьми должны строиться \nа) на предварительной взаимной договоренности; \nб) в зависимости от обстоятельств. "
user_naber_57 = "57. Когда звонит телефон, Вы \nа) торопитесь подойти первым; \nб) надеетесь, что подойдет кто-нибудь другой. "
user_naber_58 = "58. Что Вы цените в себе больше \nа) развитое чувство реальности; \nб) пылкое воображение. "
user_naber_59 = (
    "59. Вы больше придаете значение \nа) тому, что сказано; \nб) тому, как сказано. "
)
user_naber_60 = "60. Вы в основном считаете себя \nа) трезвым и практичным; \nб) сердечным и отзывчивым. "
user_naber_61 = "61. Что выглядит большим заблуждением \nа) излишняя пылкость, горячность; \nб) чрезмерная объективность, беспристрастность. "
user_naber_62 = "62. Какие ситуации привлекают Вас больше \nа) регламентированные и упорядоченные; \nб) неупорядоченные и нерегламентированные. "
user_naber_63 = "63. Вы человек, скорее \nа) педантичный, чем капризный; \nб) капризный, чем педантичный. "
user_naber_64 = "64. Вы чаще склонны \nа) быть открытым, доступным людям; \nб) быть сдержанным, скрытным. "
user_naber_65 = "65. В литературных произведениях Вы предпочитаете \nа) буквальность, конкретность; \nб) образность, переносный смысл. "
user_naber_66 = "66. Что для Вас труднее \nа) находить общий язык с другими; \nб) использовать других в своих интересах. "
user_naber_67 = "67. Чего бы вы себе больше пожелали \nа) ясности размышлений; \nб) умения сочувствовать. "
user_naber_68 = (
    "68. Что хуже \nа) быть неприхотливым; \nб) быть излишне привередливым. "
)
user_naber_69 = "69. Вы предпочитаете \nа) запланированные события; \nб) незапланированные события. "
user_naber_70 = "70. Вы склонны поступать скорее \nа) обдуманно, чем импульсивно; \nб) импульсивно, чем обдуманно."


choice = inline()


####################################КЛЮЧИ########################################
def add_key(key):
    string = f"""
Теперь напишите или пришлите мне сообщение, которое нужно сохранить для закладки:
`{key}`
"""
    return string


def remove_key(key):
    string = f"""
Закладка `{key}` удалена!
"""
    return string


add_key_error = (
    "Не удалось добавить сообщение в закладки. Пожалуйста, повторите попытку позже."
)
add_key_successful = "Сообщение успешно сохранено!"
get_key_error = "Не удалось найти в закладках это название. Пожалуйста, проверьте закладки командой /list."
get_key_error2 = "Сообщение было удалено. К сожалению, к нему больше нету доступа."
list_key_error = "У Вас ещё нету закладок!"
remove_key_error = "Не удалось найти в закладках это название. Пожалуйста, проверьте закладки командой /list."
