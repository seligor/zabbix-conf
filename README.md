Мониторинг процессов ST с помощью zabbix
Используется активный агент. То есть сам агент собирает данные о процессах
файл [.conf](https://github.com/seligor/zabbix-conf/blob/master/st7_metrics.conf)

Шаблон для визуализации полученных данных
На самом деле интересует не столько абсолютная величина значений, сколько статистические отклонения
файл [.yaml](https://github.com/seligor/zabbix-conf/blob/master/zabbix_FG7_monitoring.yaml)


Внимание, шаблон и конфиг мониторят 7 версию ST (есть изменения в наименованиях процессов относительно более старых версий)
Для использования необходимо в основной конфиг агента добавить директиву для загрузки скачанного конфига или добавить содержимое скачанного конфига в основной

Так же необходимо импортировать готовые шаблоны в ваш zabbix сервер, после чего приенить эти шаблоны к серверу, показатели которого нужно мониторить. 

Проверка наличия свежей версии
[version_check](https://github.com/seligor/zabbix-conf/tree/master/version_check)
1. Поместить st_site_check.py в директорию /usr/lib/zabbix/externalscripts для того, чтобы он вызывался шаблоном. 
2. Шаблон позволяет контролировать версию ST на сервере (по API запросу) и наличие актуальной версии. 
Ссылка на файл с информацией об актуальной версии может поменяться. Актуальную ссылку можно запросить у поддержки. 

Проверка обновлений ST
[check_updates](https://github.com/seligor/zabbix-conf/tree/master/check_updates)
1. Позволяет сравнить версию установленную на вашем сервере с опубликованнйо версией, доступной на сайте.
2. Позвоняет записать в инвентаризацию сервера информацию об изменениях ST добавленных относительно установленной версии
