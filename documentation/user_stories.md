# Käyttäjätarinat

| ID  | As a/an | I want to...                        | So that...                                                          | WORKING/TODO |
| --- | ------- | ----------------------------------- | ------------------------------------------------------------------- | ------------ |
| 1   | user    | add a new recipe                    | others can prepare it                                               | DONE         |
| 2   | user    | comment on other users' recipes     | they get good critic on it and everyone knows if the recipe is good | DONE         |
| 3   | user    | vote for other users' recipes       | everybody can see quickly, if the recipe is good                    | DONE         |
| 4   | user    | search recipes by category          | I can find recipes of my liking                                     | DONE         |
| 5   | admin   | remove bad comments                 | no harm is caused by malicious users                                | SCRAPPED     |
| 6   | admin   | ban users                           | no harm is caused by malicious users                                | SCRAPPED     |
| 7   | admin   | remove malicious/incomplete recipes | recipebook doesn't get ploated with useless recipes                 | SCRAPPED     |
| 8   | admin   | have access to users' emails        | I can contact them in problematic cases                             | SCRAPPED     |

## SQL-kyselyt tarinoille

### 1

`INSERT INTO recipe(name, ingredients, recipe_text, tips) VALUES ();`

### 2

`INSERT INTO comment(text) VALUES ();`

### 3

`INSERT INTO vote(user_id, recipe_id) VALUES ()`

### 4

`SELECT recipe.id, recipe.name, recipe.account_id FROM recipe LEFT JOIN recipe_category ON recipe_category.recipe_id = recipe.id LEFT JOIN category ON category.id = recipe_category.category_id WHERE category.id = ?`
