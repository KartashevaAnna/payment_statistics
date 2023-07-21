# payment-statistics

Как подключать миграции:
1) poetry add aerich
2) aerich init -t app.db_config.db_config
3) aerich init-db
4) aerich migrate --name remove_company_email - создать новую миграцию
5) aerich upgrade - применить ее
6) aerich downgrade - откатить назад либо aerich downgrade с указанием версии, на которую откатываемся
