﻿default group_score = 0
default anya_score = 0
default vladimir_score = 0
default platon_score = 0
default performance = 0
default act1_ending = 0

label start:
    $ mc_name = "Пекус"
    $ vladimir_name = "Какой-то парень"
    $ platon_name = "Какой-то парень"
    $ anya_name = "Какая-то девушка"

    scene railway_station

    "Железнодорожный вокзал утопал в утреннем свете."

    "Его двери распахивались, как широкие ворота в другой мир, где дороги и судьбы переплетались."

    mc "{thoughts}И вот я здесь!{/thoughts}"

    mc "{thoughts}Так-с, теперь нужно как-то добраться до ВУЗа…{/thoughts}"

    scene phone

    "Из правого кармана кофты ты достал телефон и, сделав пару быстрых движений пальцами, открыл на нем карту. На телефоне была видна тонкая ломаная - это была дорога до твоей общаги."

    mc "{thoughts}Да, далековато… Пожалуй, вызову такси.{/thoughts}"

    scene black

    show text "Спустя 30 минут (Едем на такси)" at truecenter with dissolve
    pause 3.0
    hide text

    scene collegetown

    mc "{thoughts}Итак, я в Студенческом городке. Пора заселяться!{/thoughts}"

    scene black

    show text "Спустя еще 30 минут (Проходим процесс Заселения)" at truecenter with dissolve
    pause 3.5
    hide text

    scene dormitory_corridor

    mc "{thoughts}Документы на проживание у меня, проживание я оплатил - осталось увидеть комнату!{/thoughts}"

    mc "{thoughts}И, возможно, моего соседа… Лишь бы кто-нибудь нормальный попался…{/thoughts}"

    scene black

    scene dormitory_room

    "На двери была цифра 257. Ты заходишь в комнату. Это была самая обычная комната на два человека. В комнате было два шкафа, две тумбочки, две кровати и холодильник."

    "Одна половина комнаты была уже кем-то занята. Все в той половине говорило, что этот человек тут достаточно давно."

    "Вдруг за спиной послышались чьи-то шаги. Они становились все ближе и ближе, пока сзади тебя не показался высокий силуэт."

    show vladimir_smile

    vladimir "Приятно познакомиться, меня зовут Владимир, можешь звать просто Вовой! Я - председатель ССК №11 Скорее всего, для тебя это сейчас просто какие-то слова… Ну ладно, что-то я заговорил тебя. Тебя-то, кстати, как зовут?"
    $ vladimir_name = "Владимир"

    $ mc_name = renpy.input("Придумайте имя:")

    vladimir "красивое имя, мне нравится! Что ж, добро пожаловать в общежитие №11! Теперь ты - член нашей семьи. А мы семью не бросаем! Ты, кстати, с какого института?"

    "Ты чувствуешь себя очень неловко и тебе сложно связать даже два слова. Тем не менее, набравшись сил, ты сказал Владимиру о своем институте."

    vladimir "О, РадиоФак…"

    show vladimir_smile

    vladimir "Радистов у нас еще не было!"

    "Только ты захотел разложить вещи, как вдруг что-то завибрировало в кармане."

    mc "{thoughts}Что же на этот раз?{/thoughts}"

    scene phone

    "“Вы были приглашены в беседу РИ-150954”."

    mc "{thoughts}Ого, уже даже группу создали. Надо бы почитать, что там творится.{/thoughts}"

    show text "Чат в телефоне" at truecenter with dissolve
    pause 1.5
    hide text

    anya "Всем Привет! Я - Аня и я намерена провести этот год максимально круто! Давайте знакомиться! ^_^"

    platon "Ку"

    andrey "Всем привет, дорогие первокурсники! Меня зовут Андрей и я - наставник вашей академической группы."

    andrey "Как я понимаю, большая часть группы заселилась, а значит пришла пора нам всем увидеться и познакомиться! Через полчаса жду всех у ГУКа (Мира, 19)."

    "Прочитав это сообщение, ты поддаешься смущению и неловкости."

    scene mirror

    mc "{thoughts}Блин, а что, если я как-то не так выгляжу? Волосы нормально уложены? Обувь чистая?{/thoughts}"

    "Немного постояв у зеркала, ты успокоился и решительно двинулся к выходу из комнаты."

    vladimir "Уже побежал? Ну давай, удачи!"
    hide vladimir_smile

    scene black

    show text "спустя 15 минут (Идем в гук)" at truecenter with dissolve
    pause 3.0
    hide text

    scene guk_outside

    "Подходя туда, ты замечаешь величественное здание перед собой. Казалось, эти колонны стоят там сотни, нет, тысячи лет."

    "Эти старые деревянные двери, казалось, вели в совсем другой мир, мир, где царят свои законы и правила. Ты боишься попасть туда, в тот самый дивный новый мир. Но тебе придется…"

    "На площади перед этим громадным зданием собирались группы людей."

    mc "{thoughts}Хех, похоже, мы не одни такие.{/thoughts}"

    "Увидев табличку с надписью “РИ-150954”, ты испытываешь еще большое смущение, твое сердце бьется так сильно, будто вот-вот выскочит из груди, а на щеках проступили красные пятна."

    "ты подходишь к этим людям. Все они стояли в кругу, а эту табличку держал среднего роста парень с темными кудрявыми волосами и ореховыми глазами."

    show andrey_base

    mc "{thoughts}Та-а-ак, это, скорее всего, Андрей.{/thoughts}"

    andrey "Как ты уже, наверное, понял, я тот самый Андрей. Приятно познакомиться! А как тебя зовут?"

    "Ты называешь свое имя. Кто-то засмеялся, кто–то пропустил это мимо ушей, а кто-то просто принял это как данность. От всех этих реакций ты выпадаешь из реального мира…"

    "Ты бы и дальше стоял отлученный от этого мира, если бы тебя никто не трогал. Но не тут-то было…"

    hide andrey_base

    anya "Посторони-и-и-ись!"
    $ anya_name = "Аня"

    show andrey_base at left
    show anya_base at right

    "В тебя врезалась какая-то девушка. Она была среднего роста, с голубыми глазами. Красные крашеные волосы, длинные ресницы - она завораживала собой."

    "Ее одежда была очень яркая. Помимо этого, было в ней что-то притягивающее, что-то такое, что давало людям силу и вдохновение."

    menu:
        anya "Всем привет!!! Меня зовут Аня! И в мои планах провести ближайшие четыре года незабываемо круто! Ты, кстати, как? Не сильно я тебя приложила?"

        "Протянуть руку":
            $ anya_score += 1

            mc "Да, все нормально. Будем знакомы!"

            "Ты протянул ей руку. Она с огнем в глазах пожала ее, а на лице Ани выступила улыбка, в которой, казалось, можно было утонуть. (1 выбор - +репутация у Ани)"

            anya "Хехе..."

        "Разозлиться":
            $ anya_score -= 1

            mc "Аккуратней надо быть! Не хватало мне еще в первый день оказаться в больнице."

            anya "Прости… Я просто немного не справилась с управлением…"

            "после этой перекидки фразами в воздухе повисла долгая тишина. Всем сразу стало некомфортно и неудобно. (2 выбор - -репутация у Ани)"

    andrey "Так, хватит буянить, вставайте в круг быстрее! Сейчас будем знакомиться поближе!"

    hide anya_base
    hide andrey_base

    "Вы поиграли во множество игр на сближение и сплочение группы."

    andrey "Итак, теперь, когда мы все познакомились, пора провести вас по главным точкам! Пойдемте за мной!"

    scene black

    show text "Идем в ГУК" at truecenter with dissolve
    pause 1.5
    hide text

    scene guk_outside

    "Андрей повел вас в то самое вековое здание. Открыв те самые двери, ты увидел прекрасный интерьер. Кофейня, гранитные лестницы, позолоченные двери - все это сочеталось друг с другом и создавало впечатление уютного места."

    show andrey_base

    andrey "Это Главный Учебный Корпус или же ГУК. Здесь у вас буду проходить пары, а также различные мероприятия."

    andrey "Это одно из самых красивых зданий в УрФУ, советую вам как-нибудь по нему прогуляться."

    mc "{thoughts}Вау, ну и красота… Все такое громадное, будто сделано для великанов.{/thoughts}"

    andrey "Так, теперь все вместе идем в радик."

    scene black

    show text "Идем в радик" at truecenter with dissolve
    pause 1.5
    hide text

    scene rtf_outside

    show andrey_base

    andrey "А это - здание нашего института. Тут у нас находятся наш деканат, союз студентов ИРИТ-РТФ и много всего другого."

    andrey "Большинство ваших пар будут проходить в этих двух зданиях: в ГУКе и в Радиофаке.  Есть еще много различных институтов и зданий, связанных с УрФУ, но о них вы узнаете потом."

    andrey "Есть у кого вопросы?"

    show andrey_base at left
    show anya_base at right

    anya "А что за союз студентов?"

    andrey "Хороший вопрос. Тебя, кажется, Аня, зовут? Так вот, Аня, союз студентов помогает студентам, особенно вам, первокурсникам, добиться своих целей и претворить свои желания в жизнь. Позже вам об этом еще расскажут сами сотрудники проф.союза."

    andrey "в каждой академической группе должно быть три очень важных человечка, помимо наставников."

    andrey "Первый важный человечек - это староста. Человек, который связывает вас, академическую группу, и деканат. Все его поручения и просьбы должны исполняться беспрекословно."

    andrey "Если у вас есть какие-либо проблемы, связанные с обучение, староста - один из первых людей, к кому надо обратиться."

    andrey "Есть желающие стать старостой?"

    "Кто-то один поднял руку."

    andrey "Больше желающих нет? Что ж, теперь ты староста своей группы!"

    andrey "Идем дальше. Следующим важным человечком является Проф.Орг. В его задачи входит информировать вас обо всем, что связано с Проф.Бюро - важными людьми в союзе студентов."

    andrey "Работенка непыльная и дает много разных плюшек. Есть Желающие?"

    anya "Я!"

    "Аня подняла руку. Ее глаза загорелись, а руки тянулись так, будто скоро совсем оторвуться."

    andrey "Что ж, на том и порешим! Теперь Аня - наш Проф.Орг! Давайте похлопаем!"

    andrey "А третьим важным человеком является Спорт.Орг. Он передает вам всю информацию по поводу спорта в УрФУ, будь то соревнования, тренировки и тому подобное. Кто-то хочет стать Спорт.оргом."

    "Какой-то парень поднял свою руку."

    andrey "Что ж, тогда ты Спорт.Орг!"

    andrey "Теперь, когда все главные места в группе определены, предлагаю просто прогуляться и поговорить!"

    scene collegetown

    "вы всей группой пошли гулять по студ.городку. Со временем ты стал меньше стесняться и даже попытался поднять какую-то тему. Но тебя не услышали…"

    show text "Спустя 15 минут" at truecenter with dissolve
    pause 1.5
    hide text

    "Оглядываясь вокруг, ты удивлялся каждому новому зданию. Они настолько высоки, что тебе приходилось поднимать голову вверх."

    "Позади всей группы шел один парень. Шатен, карие глаза, среднее телосложение и рост -  он выглядел как самый обычный, непримечательный юноша."

    "Вы встретились взглядами. Тебе стало жутко неловко, а по спине пробежал холод. Парень начал идти в твою сторону."

    show platon_base

    platon "Я видел твой взгляд. Хочешь познакомиться?"

    mc "{thoughts}Черт, ну я и дебил…{/thoughts}"

    mc "Да, конечно!"

    "Ты всем своим видом стараешься не показывать свое неудобство и стыд перед ним. Ты назвал свое имя."

    platon "Ну, имя как имя. А меня зовут Платон. Будем знакомы!"
    $ platon_name = "Платон"

    "Ты стал искать общие темы для разговора. Платон отвечал на все твои вопросы максимально прямолинейно."

    "В какой-то момент речь зашла о Союзе Студентов и внеучебной деятельности. Ты спросил его, как он к всему этому относится."

    platon "Я считаю, что все это бесполезно. Лично я пришел сюда просто учиться и в будущем получить высшее образование. Эта игра в друзяшек и в взаимопомощь мне неинтересна. Лучше бы уж просто учились…"

    "Ты попытался переубедить Платона, но он стоял на своем. Попытавшись пару-тройку раз, ты сдался и решил не лезть туда, куда тебя не просят."

    show text "Спустя еще 15 минут" at truecenter with dissolve
    pause 2.0
    hide text

    hide platon_base

    show andrey_base

    andrey "я думаю, на сегодня хватит. Можете расходиться или можете гулять дальше. Ну а я вас покидаю. Всем пока!"

    "Андрей быстро пропал из твоего поля зрения. Платон и большая часть группы разошлась, остались только самые активные, такие как Аня. Ты стал думать о том, остаться или нет. Остановившись на месте, ты стал смотреть вслед остаткам группы."

    scene black

    menu:
        "Гулять дальше":
            $ group_score += 1

            mc "Стойте, подождите меня"

            "Все обернулись и накинулись на тебя взглядами. Тебе стало немного не по себе, но не так сильно, как раньше."

            scene black

            "Ты догнал их и вы продолжили гулять. Среди всей этой группы Аня сильно выделялась. Она постоянно находила такие темы для разговора, которые интересовали каждого."
            "Спустя полчаса все окончательно разошлись и ты пришел обратно в свою комнату."

        "Пойти домой":
            $ group_score -= 1

            "Ребят, мне тоже надо идти. Всем пока!"

            "прощаясь, ты испытывал неловкость."

            scene dormitory_room

            "спустя полчаса ты оказался в своей комнате."

    scene dormitory_room

    "Наступил вечер. Хоть на улице и было светло, как днем, время было позднее."

    mc "{thoughts}Так, Андрей там что-то скидывал в группу, надо посмотреть.{/thoughts}"

    "Разблокировав телефон и посмотрев беседу, ты увидел какой-то план."

    scene phone

    mc "А что это такое?"
    
    andrey "Это план на ближайшие две недели. Из основного: первые две недели мы не учимся, а адаптируемся к студенческой жизни…"
    
    andrey "Также у вас будет выбор предметов в Modeus. По этому поводу могу сказать только одно - молитесь…"
    
    andrey "Из мероприятий в первые две недели будут День Первокурсника, Пикник IT и Неделя первокурсников. Это очень офигенные и крутые мероприятия, советую всем сходить…"
    
    andrey "На этом у меня все. Тусуйтесь, кайфуйте, живите!"

    "Прочитав это и полистав чат группы, ты решил пойти спать."

    show text "На следующий день" at truecenter with dissolve
    pause 1.5
    hide text

    scene dormitory_room

    "Ты проснулся. Сделав все свои утренние дела, ты оделся и вышел в сторону своего института."

    scene rtf_outside

    show andrey_base

    "Подходя к своему институту, ты вновь увидел Андрея с табличкой и свою группу. Поздоровавшись со всеми, ты пытался поговорить с ними. В этот раз кто-то из группы ответил тебе и вы что-то обсуждали до одного момента…"

    andrey "Так, РИ-150954, за мной!"

    scene rtf_outside

    "Вы всей группой зашли в здание института и ты увидел прекрасный синий интерьер. Этот интерьер привлекал каждого, кто заходил в это здание."

    scene black

    "Слева ты увидел какой-то макет. Этот макет выглядел, как очень масштабный проект. Снизу было что-то написано."

    scene black

    "вы спустились на нулевой уровень. Там тебя ждала деревянная позолоченная дверь. Она выделялась среди всех дверей на этом уровне."

    show andrey_base

    andrey "Это Р-044 или же Коворкинг. Здесь вы можете поработать или побывать на каком-либо мероприятии."

    scene black

    "Вы расселись по местам. Рядом с тобой сел Платон. Он выглядел чуть-чуть недовольным."

    "вдруг перед вами появился какой-то важный мужчина в костюме. Он что-то рассказывал, но ты его почти не слушал."

    show platon_base

    mc "Слушай, а кто это?"

    platon "Обабков Илья Николаевич, Директор ИРИТ-РТФ."

    mc "{thoughts}Ого, такая важная фигура нашего института.{/thoughts}"

    "После рассказа вам дали много вещей от партнеров и вы вышли из этого прекрасного здания."

    hide platon_base

    show andrey_base at right

    andrey "Так, теперь мы идем на День Первый! Все, кто не хотят, могут не идти!"

    scene first_day

    "Вы подошли к площади перед главным учебным корпусом. Вы увидели длинную очередь. Казалось, что эта очередь бесконечна  и что вы вряд ли попадете на День Первый."

    "Очередь кончилась и ты попал на площадь. Здесь все было, как в сказке. Красочные стенды, радостные и улыбающиеся люди и огромная прекрасная сцена."

    mc "{thoughts}Ну, пойдем изучать это все!{/thoughts}"

    "Ты начал обходить все стенды. Было много как партнеров УрФУ, так и организаций внутри самого университета. В каждой точке было что-то свое, что-то такое, чего не было у других."

    menu:
        "Пока ты ходил, на сцене выступала какая-то кавер-группа. Обойдя все стенды и побродив еще немного, ты увидел Аню."

        "Окликнуть Аню":
            "Твое сердце затрепетало, а на лбу проскочил пот. Ты собрался с силами и выкрикнул ее имя."

            mc "Аня!"

            show anya_smile

            "Услышав свое имя, Аня незамедлительно обернулась. Ее глаза были полны детской радости и веселья."

            anya "О, [mc_name]! Не думала встретить тебя. Раз уж ты здесь, не хочешь прогуляться вместе?"

            "Предложение Ани выбило тебя из колеи. Но по ее виду было понятно, что она взорвется, если не услышит ответ."

            hide anya_smile

            menu:
                "А почему бы и нет? Пойдем!":
                    $ anya_score += 1

                    "В процессе прогулки вы поднимали много различных тем и обсуждали их. В какой-то момент тебе стало интересно прошлое Ани."

                    mc "Аня, а почему ты такая активная и хочешь везде участвовать?"

                    show anya_sad

                    "Улыбка на лице Ани спала. На ее лице появились, скорее, грусть и тоска."

                    anya "Хе… Это долгая история. Готов слушать меня?"

                    "Ты кивнул Ане."

                    anya "Тогда, начнем с моего детства. Как бы странно это ни звучало, в детстве я была замкнутым ребенком. Родилась я в маленьком городке, тысяч 50 населения…"

                    anya "Большинство взрослых и детей там всегда были какие-то угрюмые и неразговорчивые. Заговорить с ними для меня было проблемой мирового масштаба. А найти друзей и подавно. Я сдалась и стала одной из них…"

                    anya "стать одной из тех, кто будет открыт ко всем и кто будет радовать людей вокруг!"

                    "Послушав рассказ Ани, ты сильно удивился, но не показал этого. После этого разговора вам стало некомфортно."

                    anya "Я тогда пойду. Увидимся!"

                "Не, я как-нибудь сам.":
                    "Тебе стало очень неловко. Ты был готов провалиться сквозь землю."

                    anya "Ну ладно, увидимся!"

                    "Отказ никак не сказался на состоянии Аня и она дальше побежала изучать стенды."

        "Пройти мимо":
            "Ты прошел мимо Ани."

            scene black

    scene black

    "ближе к вечеру мероприятие кончилось. Ты был доволен тем, что пришел сюда."

    scene dormitory_room

    show vladimir_base

    "Вернувшись в комнату, Владимир смотрел на тебе любопытным взглядом."

    mc "Володя, что-то не так?"

    vladimir "Мне очень интересно узнать твое мнение про День Первый."

    "Ты рассказал Владимиру все, что происходило на мероприятии. В глазах соседа было видно умиление и наслаждение."

    vladimir "повезло же тебе. Я вот не смог туда попасть. Дела, дела и еще раз дела…"

    vladimir "Ну ладно, сейчас не об этом. Кушать не хочешь?"

    "В руках Владимира неожиданным образом появилась сковородка с жареными пельменями. Увидев их, ты облизнулся."

    menu:
        vladimir "Ну ладно, сейчас не об этом. Кушать не хочешь?"

        "Согласиться":
            $ vladimir_score += 1

            mc "А давай!"

            "Вы поели вместе с Владимиром. После перекуса вы разговаривали на разные темы. Было видно, что Владимир рад такому общению."

        "Отказаться":
            mc "Нет, пожалуй, откажусь."

            "На лице Владимира проступила еле заметная печаль. Пока он ел пельмени, ты сидел в телефоне. В комнате была гробовая тишина. (2 выбор)"

    scene black

    if anya_score > 0 and vladimir_score > 0:
        $ act1_ending = 1
        "Прошло четыре дня. Все это время ты переписывался с группой и общался с Аней и Владимиром. Кто-то даже скинул фотку казана, полного плова."
        "В результате эти двое стали первыми людьми, с которыми ты мог говорить спокойно."

    elif anya_score > 0:
        $ act1_ending = 2
        "Прошло четыре дня. Все это время ты переписывался с группой. Ближе всех из группы ты знал Аню."
        "А вот с Владимиром ты почти не разговаривал. Из-за тебе было очень некомфортно в своей же комнате."

    elif vladimir_score > 0:
        $ act1_ending = 3
        "Прошло четыре дня. Хоть ты и познакомился с группой, общаться с ними ты не видел никакого смысла. Вместо этого ты общался с Владимиром и узнал много чего нового про студенческую жизнь. (3 исход +реп у Владимира, условие - +1 у Владимира)"

    else:
        $ act1_ending = 4
        "Прошло четыре дня. Ты не посчитал нужным с кем-либо общаться."

    jump act2
