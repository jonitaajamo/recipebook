## CREATE TABLE -lauseet

`CREATE TABLE account ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, email VARCHAR(144) NOT NULL, username VARCHAR(144) NOT NULL, password VARCHAR(144) NOT NULL, admin BOOLEAN NOT NULL, PRIMARY KEY (id), CHECK (admin IN (0, 1)) );`

`CREATE TABLE category ( id INTEGER NOT NULL, name VARCHAR(144) NOT NULL, PRIMARY KEY (id) );`

`CREATE TABLE recipe ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, name VARCHAR(144) NOT NULL, ingredients VARCHAR(500) NOT NULL, recipe_text VARCHAR(1000) NOT NULL, tips VARCHAR(500), public BOOLEAN NOT NULL, account_id INTEGER NOT NULL, PRIMARY KEY (id), CHECK (public IN (0, 1)), FOREIGN KEY(account_id) REFERENCES account (id) );`

`CREATE TABLE comment ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, text VARCHAR(500) NOT NULL, recipe_id INTEGER NOT NULL, account_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY(recipe_id) REFERENCES recipe (id), FOREIGN KEY(account_id) REFERENCES account (id) );`

`CREATE TABLE recipe_category (
recipe_id INTEGER NOT NULL,
category_id INTEGER NOT NULL,
PRIMARY KEY (recipe_id, category_id),
FOREIGN KEY(recipe_id) REFERENCES recipe (id),
FOREIGN KEY(category_id) REFERENCES category (id)
);``

`CREATE TABLE vote ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, account_id INTEGER NOT NULL, recipe_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY(account_id) REFERENCES account (id), FOREIGN KEY(recipe_id) REFERENCES recipe (id) );`
