-- Solución de tarea_33
-- Autor: Juan Pablo Salado
-- Realizado: 2021-05-15

-- Tarea: "Un cracker ha accedido a una información privada y tú, que eres "El inspector SQL", debe tomar
-- una serie de decisiones mediante sentencias SQL para resolver el caso". Escribe en un documento de
-- texto (.doc, .txt, ...) la sentencia SQL que has utilizado para cada caso resuelto junto con una breve
-- explicación sobre la sentencia que has utilizado.
-- Aunque es un ejercicio sencillo y no profundiza puede ser suficiente para que veáis como se trabaja con
-- SQL. No se os pide que os registréis, únicamente que asimiléis estructuras de programación SQL y que
-- lo documentéis. Diviértete:

-- LINK: https://sqlpd.com/

-- La tarea consiste en el uso de terminos SQL de selección, limitación y ordenado de datos. A continuación las soluciones para los distintos casos.

-- Enunciado 1: A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all entries' details.
-- Solución:
 SELECT * FROM mailing_list;

-- Enunciado 2: An illegal site's servers were seized in a recent operation. Please submit all users' details.
-- Solución:
SELECT * FROM users;

-- Enunciado 3: An illegal site's servers were seized in a recent operation. Please submit all users number of downloads, emails and surnames' details.
-- Solución:
SELECT Surname, Email, Downloads FROM users;

-- Enunciado 4: An illegal site's servers were seized in a recent operation. Please submit all users first names, number of posts and email addresses' details.
-- Solución:
SELECT Firstname, Posts, EmailAddress FROM users;

-- Enunciado 5: A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all entries join dates' details. Please make sure there are no duplicates.
-- Solución:
SELECT DISTINCT JoinDate FROM mailing_list;

-- Enunciado 6: An illegal site's servers were seized in a recent operation. Please submit all users' details sorted by last names in ascending order.
-- Solución:
SELECT * FROM users ORDER BY LastName ASC;

-- Enunciado 7: An illegal site's servers were seized in a recent operation. Please submit all users' details sorted by last access times in descending order.
-- Solución:
SELECT * FROM users ORDER BY LastAccess DESC;

-- Enunciado 8: An illegal site's servers were seized in a recent operation. Please submit all users number of downloads, given names and last access times' details sorted by last access times in descending order. Please make sure there are no duplicates.
-- Solución:
SELECT DISTINCT Downloads, GivenName, LastAccess FROM users ORDER BY LastAccess DESC;

-- Enunciado 9: A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all entries emails, family names and given names' details sorted by family names in descending order and then by emails in ascending order.
-- Solución:
SELECT Email, FamilyName, GivenName FROM mailing_list ORDER BY FamilyName DESC, Email ASC;

-- Enunciado 10: White hat hacker has sent SQLPD exposed members' details of a shady site connected to various persons of interest. Please submit the top 20 members' details when sorted by usernames in ascending order and then by full names in descending order.
-- Solución:
SELECT * FROM members ORDER BY Username ASC, FullName DESC LIMIT 20;

-- Enunciado 11: A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit the top 3 records given names and emails' details when sorted by emails in descending order and then by given names in ascending order. Please make sure there are no duplicates.
-- Solución:
SELECT DISTINCT GivenName, Email FROM mailing_list ORDER BY Email DESC, GivenName ASC LIMIT 3;
