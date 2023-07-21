CREATE TABLE IF NOT EXISTS "payment_statistics"."company" (
"id" UUID NOT NULL  PRIMARY KEY,
"org_type" varchar(16),
"name" varchar(256),
"inn" varchar(15),
"current_account" varchar(20),
"activity" varchar(256),
"logo_url" varchar(256),
"email" varchar(128),
"phone_number" varchar(11),
"status" varchar(16) NOT NULL,
"is_sanctioned" BOOL,
"site_url" varchar(256)
);
CREATE TABLE IF NOT EXISTS "payment_statistics"."user"(

);