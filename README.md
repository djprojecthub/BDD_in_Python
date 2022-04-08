# BDD_in_Python
In an Agile development framework, BDD creates a culture where testers, developers, business analysts and other
stakeholders of the project can contribute towards the software development.

![1_V3CyC87v-5oj6icmWeu-fg](https://user-images.githubusercontent.com/70992215/162369988-1cc95351-2222-43ae-b3c2-bfcaa8e2dd2e.jpg)

Behave is a tool used for BDD in Python programming language.

Behave has tests developed in plain text with the implementation logic in Python.

1. **Behave works with three different file types** :
 
    1. **Feature file** which are created by a Business analyst or any project stakeholder
       and contains behavior related use cases.
    2. **Step implementation file** for the scenarios define in the feature file.
    3. **Environment setup file** where, the pre/post conditions are to be executed
       prior and post the steps, features, scenarios, and so on.

2.  **Gherkin language keywords in Behave** :

    1. **Feature** : Short description of feature being tested.
    2. **Background** : Used for executing preconditions like login Scenarios or
        database connection, and so on. It can appear only a single time in
        a feature file and it must be declared prior to a Scenario or Scenario
        outline.
    3. **Scenario** :
         a. Defines behaviour of the application that is being tested.
         b. It has multiple steps which begins with keyword Given, Then,
            When, and so on.
         c. It checks a single characteristic or an expected result.
    4. **Scenario Outline** :
         a. It is used when we have group of similar criteria and the results
            to be passed in a scenario.
         b. It is accompanied with an Examples table and can have multiple
            Examples tables.
         c. The tests gets executed once for every row found after the header
            row within the Examples table.
         d. The values to be tested are represented by their name enclosed in
            brackets<>. These names should match with the Examples table header.
    5. **Given** : It is used to place the system in a familiar circumstance prior to
       the interaction of the user with the system.
    6. **When** : It is used to add the essential task to be performed by the user.
    7. **Then** : It is used to get the expected results.
    8. **And, But** : Use them for better readability when we have multiple Given,
       When, Then consecutive steps.

3.  **Context in behave** :
    1.  Context is a very important feature in Python Behave where the user and Behave
    can store information to share around.
    2.  It holds the contextual information during the execution of tests.
    3.  It is an object that can store user-defined data along with Python Behave-defined data, in context attributes.

4.  **BDD vs TDD**

    ![1605538881-2](https://user-images.githubusercontent.com/70992215/162370306-1bf8358b-b35c-4fa5-9b96-3865c1b868a9.png)


