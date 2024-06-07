# In this file you must implement your main query methods 
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

# note that your remote host where your database is hosted
# must support user permissions to run stored triggers, procedures and functions.
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]



def connect():
        """
        This method creates a connection with your database
        IMPORTANT: all the environment variables must be set correctly
                   before attempting to run this method. Otherwise, it
                   will throw an error message stating that the attempt
                   to connect to your database failed.
        """
        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            print("Bot connected to database {}".format(db_name))
            return conn
        except ConnectionError as err:
            print(f"An error has occurred: {err.args[1]}")
            print("\n")

    #TODO: needs to implement the internal logic of all the main query operations
def get_response(msg):
  db_response = None
  command_parts = msg.split()
  bot_command = command_parts[0]



  #Requirement #1
  if "!ManufacturersSellFullerene" in bot_command:
    Num_Carbon = command_parts[1]
    db_response = manufacturers_sell_fullerene(Num_Carbon)
  #Requirement #2
  elif "!researcherswhostudy" in bot_command:
    Research_Topic = command_parts[1]
    db_response = Query.researcherswhostudy(Research_Topic)
  #Requirement #3
  elif "!employeesmakebank" in bot_command:
    db_response = employees_make_bank()
  #Requirement #4
  elif "!productsusedin" in bot_command:
    Industry_id1 = command_parts[1]
    Industry_id2 = command_parts[2]
    db_response = products_used_in(Industry_id1, Industry_id2)
  #Requirement #5
  elif "!insertemployee" in bot_command:
    team_id = command_parts[1]
    db_response = insert_employee(team_id)
  #Requirement #6
  elif "!insertteam" in bot_command:
    manufacturer_id = command_parts[1]
    db_response = insert_team(manufacturer_id)
  #Requirement #7
  elif "!updateuserrole" in bot_command:
    user_id = command_parts[1]
    role_id = command_parts[2]
    db_response = update_user_role(user_id, role_id)
  #Requirement #8
  elif "!updateemployeesalary" in bot_command:
    Employee_id = command_parts[1]
    New_Salary = command_parts[2]
    db_response = update_employee_salary(Employee_id, New_Salary)
  #Requirement #9
  elif "!deleteaccount" in bot_command:
    account_id = command_parts[1]
    db_response = delete_account(account_id)
  #Requirement #10
  elif "!deleteproduct" in bot_command:
    product_id = command_parts[1]
    db_response = delete_product(product_id)
  #Requirement #11
  elif "!incrementemployees" in bot_command:
    team_id = command_parts[1]
    db_response = increment_employees(team_id)
  #Requirement #12
  elif "!deletepublications" in bot_command:
    researcher_id = command_parts[1]
    db_response = delete_publications(researcher_id)
  #Requirement #13
  elif "industrialNWproductlist" in bot_command:
    industry_id = command_parts[1]
    db_response = industrial_NW_product_list(industry_id)
  #Requirement #14
  elif "!manufacturerswhosellNW" in bot_command:
    conductivity = command_part[1]
    db_response = manufacturers_who_sell_NW(conductivity)
  #Requirement #15
  elif "!SubdivList" in bot_command:
    Name = command_parts[1]
    db_response = subdiv_list(Name)
  else:
    return "Unknown command"
  return db_response
      
@staticmethod
def select(query, values=None, fetch=True):
       database = Database()
       return database.get_response(query, values=values, fetch=fetch)
        # your code here
#Requirement 3
def employeesmakebank():
  conn = connect()
  cur = conn.cursor()
  query = Query.employeesmakebank
  cur.execute(query)


class Query:
  ManufacturersSellFullerene = """SELECT 
        c.Country_id,
        m.Manufacturer_id,
        m.Name AS Manufacturer_Name,
        f.Fullerene_id,
        f.Num_Carbon
    FROM
        Country c
    JOIN Manufacturer m ON c.Country_id = m.Country_Country_id
    JOIN Fullerene_Sold_by_Manufacturer fsm ON m.Manufacturer_id = fsm.Manufacturer_Manufacturer_id
    JOIN Fullerene f ON fsm.Fullerene_Fullerene_id = f.Fullerene_id
    WHERE
        f.Num_Carbon = user_chosen_num_carbon;"""

  researcherswhostudy = """SELECT R.Researcher_id, R.Years_Experience, R.Num_Publications
FROM Researcher R
JOIN Research_Project RP ON R.Researcher_id = RP.Researcher_id

WHERE RP.Research_Topic = 'UserResearchTopic' -- Replace 'YourResearchTopic' with the actual research topic
    AND R.Years_Experience >= 30
GROUP BY R.Researcher_id
HAVING R.Num_Publications > 10;"""

  employeesmakebank = """SELECT M.Manufacturer_id, M.Name AS ManufacturerName, E.Employee_id, E.Employee_title, E.Salary
FROM Manufacturer M
JOIN Employee E ON M.Manufacturer_id = E.Manufacturer_Manufacturer_id
WHERE M.Size >= 1000
    AND E.Salary >= 100000;"""

  productsusedin = """SELECT *
FROM Product
WHERE Product_Type = 'Commercial'
  AND Industry_id IN (:industry_id1, :industry_id2);"""

  insertemployee = """INSERT INTO Employee (Employee_id, Team_Team_id)
SELECT employee_id, team_id
FROM Team
WHERE Team_id = team_id;"""

  insertteam = """INSERT INTO Team (Team_id, Manufacturer_Manufacturer_id)
VALUES (team_id, manufacturer_id);"""

  updateuserrole = """UPDATE User
SET role_id = role_id
WHERE user_id = user_id;"""

  updateemployeesalary = """UPDATE Employee
SET Salary = NEW_SALARY
WHERE Employee_id = YOUR_EMPLOYEE_ID;"""

  deleteaccount = """DELETE FROM Account
WHERE Account_id = account_id
  AND EXISTS (SELECT 1 FROM Account WHERE Account_id = account_id LIMIT 1);"""

  deleteproduct = """DELETE FROM Product
WHERE Product_id = product_id
  AND EXISTS (SELECT 1 FROM Product WHERE Product_id = product_id LIMIT 1);"""

  incrementemployees = """CREATE TRIGGER after_insert_employee
AFTER INSERT ON Employee
FOR EACH ROW
BEGIN
    IF NEW.Team_Team_id IS NOT NULL THEN
        UPDATE Team
        SET Num_Employees = Num_Employees + 1
        WHERE Team_id = NEW.Team_Team_id;
    END IF;
END;"""

  deletepublications = """CREATE TRIGGER trg_DeletePublications
BEFORE DELETE ON Researcher
FOR EACH ROW
BEGIN
    DELETE FROM Publication
    WHERE Researcher_id = OLD.Researcher_id;
END;"""

  industrialNWproductlist = """CREATE PROCEDURE GetIndustrialNanoWProductList(IN industryId INT)
BEGIN
    SELECT
        P.Product_id,
        P.Product_Type,
        NW.Application,
        NW.Conductivity
    FROM
        Product P
    JOIN Nanowires NW ON P.Product_id = NW.Product_Product_id
   

    WHERE
        P.Industry_id = industryId
        AND P.Product_Type = 'Industrial';
END """

  manufacturerswhosellNW = """CREATE FUNCTION GetManufacturersByConductivity(conductivityType VARCHAR(45))
RETURNS VARCHAR(255)
BEGIN
    DECLARE manufacturerList VARCHAR(255);
    
    SELECT GROUP_CONCAT(DISTINCT M.Name) INTO manufacturerList
    FROM Manufacturer M
    JOIN Manufacturer_Sells_Nanowires MSN ON M.Manufacturer_id = MSN.Manufacturer_Manufacturer_id
    JOIN Nanowires N ON MSN.Nanowires_NanoW_id = N.NanoW_id
    WHERE N.Conductivity = conductivityType;
    
    RETURN manufacturerList;
END"""

  SubdivList = """CREATE FUNCTION GetSubdivisionListByIndustry(industryId INT)
RETURNS VARCHAR(255)
BEGIN
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE subdivisionName VARCHAR(45);
    DECLARE subdivisionList VARCHAR(255) DEFAULT '';
     -- Declare a cursor to fetch subdivision names
    DECLARE curSubdivisions CURSOR FOR
        SELECT SubDiv_Name
        FROM Subdivision
        WHERE Head_Industry_id = industryId;
        
	 -- Declare continue handler to exit the loop when no more rows are available
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;


    -- Check if the industryId exists
    IF NOT EXISTS (SELECT 1 FROM Industry WHERE Industry_id = industryId) THEN
        RETURN 'Invalid Industry ID';
    END IF;
   
    -- Open the cursor
    OPEN curSubdivisions;

    -- Loop through the cursor results and concatenate subdivision names
    read_loop: LOOP
        FETCH curSubdivisions INTO subdivisionName;

        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Concatenate subdivision names with a comma
        SET subdivisionList = CONCAT(subdivisionList, subdivisionName, ',');

    END LOOP;

    -- Close the cursor
    CLOSE curSubdivisions;

    -- Remove the trailing comma, if any
    SET subdivisionList = TRIM(TRAILING ',' FROM subdivisionList);

    RETURN subdivisionList;
END """