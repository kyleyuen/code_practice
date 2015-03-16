# Write your MySQL query statement below
select FirstName, LastName, City, State from Person, Address where Person.PersonId=Address.PersonId;