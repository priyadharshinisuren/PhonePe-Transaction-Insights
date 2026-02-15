import streamlit as st
import pandas as pd
import seaborn as sns
import json
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
db_URL = "postgresql://postgres:root@localhost:5432/phonepe"
engine = create_engine(db_URL)



r = st.sidebar.radio('Navigation', ['Home','Analysis'])

if r == 'Home':
    st.title("Welcome to PhonePe Pulse")
    st.image("C:/Users/priya/OneDrive/Pictures/logo.png")
    quarter =st.selectbox("Select Quarter", ["Quarter1", "Quarter2", "Quarter3", "Quarter4"],width="stretch")
    if quarter == "Quarter1":
      query = """
        SELECT
            "Quarter",
            "Transaction_count",
            ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Quarter" = 1
        LIMIT 5;
       """
      df = pd.read_sql_query(query, engine)
      st.write("Quarter 1 Transactions")
      st.dataframe(df)
      

    elif quarter == "Quarter2":
        query = """
        SELECT
            "Quarter",
            "Transaction_count",
            ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
          FROM "Agg_transaction"
         WHERE "Quarter" = 2
         LIMIT 5;
        """
        df = pd.read_sql_query(query, engine)
        st.write("Quarter 2 Transactions")
        st.dataframe(df)
        

    elif quarter == "Quarter3":
        query = """
          SELECT
            "Quarter",
            "Transaction_count",
            ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
          FROM "Agg_transaction"
          WHERE "Quarter" = 3
            LIMIT 5;
          """
        df = pd.read_sql_query(query, engine)
        st.write("Quarter 3 Transactions")
        st.dataframe(df)
        


    elif quarter == "Quarter4":
        query = """
        SELECT
            "Quarter",
            "Transaction_count",
            ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Quarter" = 4
        LIMIT 5;
         """
        df = pd.read_sql_query(query, engine)
        st.write("Quarter 4 Transactions")
        st.dataframe(df)
        
    year =st.selectbox("Select Year", ["2018", "2019", "2020", "2021","2022","2023","2024"],width="stretch")
    if year == "2018":
      query = """
        SELECT
          "Year",
        "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2018
        LIMIT 5;
        """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2018 Transactions")
      st.dataframe(df)
    elif year == "2019":
      query = """
        SELECT
      "Year",
       "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
      WHERE "Year"::int = 2019
      LIMIT 5;
      """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2019 Transactions")
      st.dataframe(df) 

    elif year == "2020":
      query = """
        SELECT
       "Year",
       "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2020
        LIMIT 5;
        """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2020 Transactions")
      st.dataframe(df) 

    elif year == "2020":
      query = """
        SELECT
      "Year",
      "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2020
      LIMIT 5;
       """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2020 Transactions")
      st.dataframe(df) 

    elif year == "2021":
      query = """
        SELECT
      "Year",
        "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2021
        LIMIT 5;
        """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2021 Transactions")
      st.dataframe(df) 

    elif year == "2022":
      query = """
        SELECT
      "Year",
       "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
         WHERE "Year"::int = 2022
        LIMIT 5;
        """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2022 Transactions")
      st.dataframe(df) 

    elif year == "2023":
      query = """
        SELECT
        "Year",
        "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2023
        LIMIT 5;
        """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2023 Transactions")
      st.dataframe(df)

    elif year == "2024":
      query = """
        SELECT
       "Year",
      "Transaction_count",
        ROUND("Transaction_amount"::numeric, 2) AS transaction_amount
        FROM "Agg_transaction"
        WHERE "Year"::int = 2024
        LIMIT 5;
      """
      df = pd.read_sql_query(query, engine)
      st.write("Year 2024 Transactions")
      st.dataframe(df) 

    
    
    query = """
    SELECT 
    "State",
    SUM("Transaction_count") AS total_transactions,
    SUM("Transaction_amount") AS total_value,
    AVG("Transaction_amount") AS total_avg_value
    FROM "Agg_transaction"
     GROUP BY "State"
     ORDER BY total_value DESC;

     """
    df = pd.read_sql(query, engine)
    
    state_mapping = {
    "telangana": "Telangana",
    "karnataka": "Karnataka",
    "maharashtra": "Maharashtra",
    "andhra-pradesh": "Andhra Pradesh",
    "uttar-pradesh": "Uttar Pradesh",
    "rajasthan": "Rajasthan",
    "madhya-pradesh": "Madhya Pradesh",
    "bihar": "Bihar",
    "west-bengal": "West Bengal",
    "odisha": "Odisha",
    "tamil-nadu": "Tamil Nadu",
    "delhi": "Delhi",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "jharkhand": "Jharkhand",
    "chhattisgarh": "Chhattisgarh",
    "assam": "Assam",
    "kerala": "Kerala",
    "punjab": "Punjab",
    "uttarakhand": "Uttarakhand",
    "jammu-&-kashmir": "Jammu & Kashmir",
    "himachal-pradesh": "Himachal Pradesh",
    "goa": "Goa",
    "chandigarh": "Chandigarh",
    "arunachal-pradesh": "Arunachal Pradesh",
    "puducherry": "Puducherry",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra & Nagar Haveli and Daman & Diu",
    "tripura": "Tripura",
    "manipur": "Manipur",
    "meghalaya": "Meghalaya",
    "nagaland": "Nagaland",
    "sikkim": "Sikkim",
    "ladakh": "Ladakh",
    "andaman-&-nicobar-islands": "Andaman & Nicobar Islands",
    "mizoram": "Mizoram",
    "lakshadweep": "Lakshadweep"
    }
    df["State_clean"] = df["State"].map(state_mapping)

    fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    locations="State_clean",
    featureidkey="properties.ST_NM",  # adjust if needed
    color="total_transactions",
    color_continuous_scale="Turbo",
  
    )

    fig.update_geos(
    fitbounds="locations",
    visible=False
    )

    fig.update_layout(
    height=900,
    width=1000,
    margin={"r":0,"t":0,"l":0,"b":0},
    
    )

    st.plotly_chart(fig, width="stretch")

elif r == 'Analysis':
    selected_case = st.selectbox(
    "Select business case study",
    options=[
        "1. Decoding Transaction Dynamics on PhonePe",
        "2. Device Dominance and User Engagement Analysis",
        "3. Insurance Penetration and Growth Potential Analysis",
        "4. Transaction Analysis for Market Expansion",
        "5. User Engagement and Growth Strategy"])
    
    if selected_case == "1. Decoding Transaction Dynamics on PhonePe":
       
        st.title("State-Level Transaction")
        st.write(" which states drive the highest transaction volumes and values")
        query = """
        SELECT 
                "State",
                SUM("Transaction_count") AS total_transactions,
                SUM("Transaction_amount") AS total_amount
                
            FROM "Agg_transaction"
            GROUP BY "State"
            ORDER BY total_amount DESC;
        """

        
        df = pd.read_sql_query(query, engine)
            
        st.line_chart(df.set_index("State")["total_transactions"])

        st.header("Quarterly Growth")
            
        query = """
        SELECT 
        "Quarter",
        SUM("Transaction_amount") AS total_value
        FROM "Agg_transaction"
        GROUP BY "State", "Quarter"
        ORDER BY "State", "Quarter";
            """
        df = pd.read_sql_query(query, engine)
        df.columns = df.columns.str.strip()

        st.bar_chart(df.set_index("Quarter")["total_value"])
        st.header(" Top 10 Transactions")
        query = """
        SELECT 
        "State",
        SUM("Transaction_count") AS total_transactions
        FROM "Agg_transaction"
        GROUP BY "State"
        ORDER BY total_transactions
        LIMIT 10;
        """
        df = pd.read_sql_query(query, engine)
        fig = px.pie(df, values="total_transactions", names="State")
        st.plotly_chart(fig)
        st.header("Highest revenue")
        query="""SELECT 
        "State",
        MAX("Transaction_amount") AS highest_revenue
        FROM "Agg_transaction"
        GROUP BY "State"
        ORDER BY highest_revenue DESC
        LIMIT 10;"""
        df = pd.read_sql_query(query, engine)
        df['highest_revenue'] = pd.to_numeric(df['highest_revenue'], errors='coerce')
        

        fig, ax = plt.subplots(figsize=(10,6))
        sns.barplot(data=df, x="State", y="highest_revenue", ax=ax)
        ax.set_title("Revenue by State")
        ax.set_xlabel("State")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)
        st.header("Lowest revenue")
        query="""
        SELECT 
        "State",
        MIN("Transaction_amount") AS highest_revenue
        FROM "Agg_transaction"
        GROUP BY "State"
        ORDER BY highest_revenue DESC
        LIMIT 10;"""
        df = pd.read_sql_query(query, engine)
       
        fig, ax = plt.subplots(figsize=(10,6))
        sns.barplot(data=df, y="State", x="highest_revenue", ax=ax)
        ax.set_title("lowest Revenue by State")
        ax.set_xlabel("Revenue")
        ax.set_ylabel("State")
        st.pyplot(fig)
    elif selected_case == "2. Device Dominance and User Engagement Analysis":
        
        query="""SELECT 
        "brand",
        SUM("registeredUsers") AS total_registered_users
        FROM "Agg_user"
        GROUP BY "brand"
        ORDER BY total_registered_users 
        limit 5;"""
        df = pd.read_sql_query(query, engine)
        st.header("Registered Users by Device Brand")
        fig, ax = plt.subplots(figsize=(8,8))
        ax.pie(df['total_registered_users'], labels=df['brand'], autopct='%1.1f%%', startangle=90)
        st.pyplot(fig)
        st.header("Transaction percentage per year")
        df = pd.read_sql_query(query, engine)
        st.write(df.columns)
        query="""SELECT "Year",
        ROUND("transaction_percentage"::numeric, 2) AS trans_percentage
        FROM "Agg_user"
        ORDER BY trans_percentage DESC
            limit 10;"""
        df = pd.read_sql_query(query, engine)
        st.bar_chart(df.set_index("Year"))
        query = """
        SELECT "State", "Year", "registeredUsers"
        FROM (
        SELECT 
            "State",
            "Year",
            "registeredUsers",
            ROW_NUMBER() OVER (PARTITION BY "Year" ORDER BY "registeredUsers" DESC) AS rn
        FROM "Agg_user"
        ) ranked
        WHERE rn <= 10
        ORDER BY "Year" DESC, "registeredUsers" DESC;
        """
        df = pd.read_sql_query(query, engine)
        st.header("Top 10 States per Year by Registered Users")
        
        chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("registeredUsers:Q", bin=alt.Bin(maxbins=20)),  # bins registeredUsers
        y="count():Q",
        color="Year:N",
        tooltip=["State", "Year", "registeredUsers"]
        ).properties(width=600, height=400)

        st.altair_chart(chart, width="stretch")
        query = """SELECT "State", SUM("registeredUsers") AS total_users
        FROM "Agg_user"
        GROUP BY "State"
        ORDER BY total_users DESC
        LIMIT 3;"""
        st.header("Top 3 states overall total user")

        df = pd.read_sql_query(query, engine)
        pie = alt.Chart(df).mark_arc().encode(
        theta="total_users:Q",
        color="State:N",
        tooltip=["State", "total_users"]
        ).properties(width=400, height=400)

        st.altair_chart(pie, width="stretch")
        st.header(" maximum registered users each year")
        query="""SELECT "State", "Year", "registeredUsers"
        FROM (
        SELECT 
            "State",
            "Year",
            "registeredUsers",
            RANK() OVER (PARTITION BY "Year" ORDER BY "registeredUsers" DESC) AS rnk
        FROM "Agg_user"
        ) ranked
        WHERE rnk = 1
        ORDER BY "Year" DESC;"""
        df = pd.read_sql_query(query, engine)
        line_chart = alt.Chart(df).mark_line(point=True).encode(
        x="Year:N",
        y="registeredUsers:Q",
        color="State:N",
        tooltip=["State", "Year", "registeredUsers"]
        ).properties(width=600, height=400)

        st.altair_chart(line_chart, width="stretch")
    elif selected_case == "3. Insurance Penetration and Growth Potential Analysis":
       st.header=("Quarterly Premiums by State")
       query="""SELECT 
       "State",
        "Year",
        "Quarter",
        SUM("insurance_amount") AS total_premium
        FROM "Agg_insurance"
        GROUP BY "State", "Year", "Quarter"
        ORDER BY "Year", "Quarter", "State";"""
       df = pd.read_sql_query(query, engine)
       
       
       fig = px.bar(
        df,
        x="Quarter",
       y="total_premium",
         color="State",
       barmode="group",
       facet_col="Year",
        title= "Quarterly Premiums by State") # separate panels for each year
       st.plotly_chart(fig,width="stretch")
       

       
       query="""SELECT 
       "State",
       "Year",
        "insurance_type",
        SUM("insurance_amount") AS total_premium,
        ROUND(
        (SUM("insurance_amount") * 100.0 / 
         SUM(SUM("insurance_amount")) OVER (PARTITION BY "State", "Year"))::numeric,
        2
        ) AS product_share_percentage
        FROM "Agg_insurance"
        GROUP BY "State", "Year", "insurance_type"
         ORDER BY "State", "Year", "insurance_type";"""
       df = pd.read_sql_query(query, engine)
       fig = px.treemap(
       df,
       path=["Year", "State", "insurance_type"],  # hierarchy: Year → State → Type
       values="total_premium",
       color="insurance_type",
       title="Insurance Product Segmentation by State and Year"
        
        )
       
       st.plotly_chart(fig,width="stretch")
       query="""SELECT "State","Year",max("insurance_amount") as highest_premium
             FROM "Agg_insurance"
              GROUP BY "State","Year"
              order by "Year" ;"""

       df = pd.read_sql_query(query, engine)
      
       chart = alt.Chart(df).mark_bar().encode(
       x=alt.X('State:N', title='State'),
        y=alt.Y('highest_premium:Q', title='Premium'),
        color=alt.Color('Year:N', scale=alt.Scale(scheme='tableau10')),
        tooltip=['State', 'Year', 'highest_premium']
         ).properties(
         width=600,
         height=400,
         title="high premiums in a particular year")
       st.altair_chart(chart, width="stretch")
       query = """
        SELECT 
          "State",
         SUM("insurance_amount") AS total_amount,
          RANK() OVER (ORDER BY SUM("insurance_amount") DESC) AS state_rank
          FROM "Agg_insurance"
          GROUP BY "State"
          ORDER BY total_amount DESC
           LIMIT 10;
         """

       df = pd.read_sql_query(query, engine)

       

       fig, ax = plt.subplots(figsize=(10,6))
       sns.barplot(x='total_amount', y='State', data=df, palette='Blues_r', ax=ax)

       ax.set_title('Top 10 Performing States by Insurance Premium Amount', fontsize=14)
       ax.set_xlabel('Total Premium Amount')
       ax.set_ylabel('State')

       st.pyplot(fig, width='stretch')
       query="""SELECT 
       "Year",
       "Quarter",
        SUM("insurance_count") AS total_policies,
        SUM("insurance_amount") AS total_premium
         FROM "Agg_insurance"
         GROUP BY "Year","Quarter"
        ORDER BY "Year", "Quarter";"""
       df = pd.read_sql_query(query, engine)

       df['period'] = df['Year'].astype(str) + ' Q' + df['Quarter'].astype(str)

# Plot grouped bar chart
       fig, ax = plt.subplots(figsize=(10,6))

       bar_width = 0.35
       x = range(len(df))

       ax.bar([i - bar_width/2 for i in x], df['total_policies'], 
       width=bar_width, label='Total Policies', color='skyblue')
       ax.bar([i + bar_width/2 for i in x], df['total_premium'], 
       width=bar_width, label='Total Premium', color='orange')

       ax.set_xticks(x)
       ax.set_xticklabels(df['period'], rotation=45)
       ax.set_title('Transaction Volume Over Time', fontsize=26)
       ax.set_xlabel('Period (Year-Quarter)')
       ax.set_ylabel('Volume')
       ax.legend()

       st.pyplot(fig, width='stretch')
    elif selected_case == "4. Transaction Analysis for Market Expansion":
       st.title("Top 10 States by Transaction ")
       query = """
      SELECT "State", SUM("Transaction_count") AS total_transactions
      FROM "map_transaction"
      GROUP BY "State"
      ORDER BY total_transactions DESC
     LIMIT 10;
       """
       df = pd.read_sql_query(query, engine)

   # Plot vertical bar chart
       fig, ax = plt.subplots(figsize=(10,6))
       sns.barplot(x='State', y='total_transactions', data=df, palette='viridis', ax=ax)

    
       ax.set_xlabel('State')
       ax.set_ylabel('Total Transactions')
       ax.tick_params(axis='x', rotation=45)

# Show chart in Streamlit
       st.pyplot(fig, width='stretch')



       st.title("Transaction Volume Over year")
       
       query = """
         SELECT "Year", SUM("Transaction_count") AS total_transactions
         FROM map_transaction
          GROUP BY "Year"
           ORDER BY "Year";
                """
       df = pd.read_sql_query(query, engine)


       fig, ax = plt.subplots(figsize=(10,6))
       ax.bar(df['Year'], df['total_transactions'], color='steelblue')

       
       ax.set_xlabel('Year')
       ax.set_ylabel('Total Transactions')
       ax.tick_params(axis='x', rotation=45)

       st.pyplot(fig, width='stretch')
       st.title("Average Transaction Value by State")
       query="""SELECT "State",
       ROUND(AVG("Transaction_amount")::numeric, 2) AS avg_txn_value
       FROM "map_transaction"
       GROUP BY "State"
       limit 10;"""
       df = pd.read_sql_query(query, engine)
       chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('State:N', sort='-y', title='State'),
        y=alt.Y('avg_txn_value:Q', title='Average Transaction Value'),
        tooltip=['State', 'avg_txn_value']
        ).properties(
         width=600,
         height=400,
           title="Average Transaction Value by State"
           )

       st.altair_chart(chart, width="stretch")
       st.title(" Top 10 Ranking transaction amounts by state")

       query="""SELECT 
             "State", 
             MAX("Transaction_amount") AS max_transaction_amount,
              DENSE_RANK() OVER (ORDER BY MAX("Transaction_amount")) AS ranked
              FROM "map_transaction"
                GROUP BY "State"
              ORDER BY ranked
              limit 10;"""
       df = pd.read_sql_query(query, engine)
       
       chart = alt.Chart(df).mark_bar().encode(
         y=alt.Y("State", sort=alt.EncodingSortField(field="ranked", order="ascending")),
         x="max_transaction_amount",
           color="ranked:N",
           tooltip=["State", "max_transaction_amount", "ranked"]
          ).properties(
            width=600,
           height=400
            )

       st.altair_chart(chart, width="stretch")




       query = """
       SELECT "Quarter", MAX("Transaction_count") AS highest_count
       FROM "map_transaction"
       GROUP BY "Quarter"
       ORDER BY "Quarter";
       """
       df = pd.read_sql_query(query, engine)

       fig = px.pie(
       df,
        values="highest_count",
        names="Quarter",
        hole=0.4,  # donut effect
       title="Highest Transaction Count per Quarter")
       st.plotly_chart(fig, width="stretch")
    
    elif selected_case == "5. User Engagement and Growth Strategy":
        st.title("1.Total Registered Users by State")
        query="""SELECT "State", SUM("registeredUsers") AS total_registered
       FROM "map_user"
       GROUP BY "State"
       ORDER BY total_registered DESC;"""
        df = pd.read_sql_query(query, engine)
        chart = alt.Chart(df).mark_bar().encode(
         x="total_registered",
         y=alt.Y("State", sort="-x"),
        tooltip=["State", "total_registered"]
         ).properties(
         width=600,
        height=400
         )
        st.altair_chart(chart,width="stretch")

        query="""SELECT "State","District", SUM("appOpens") AS total_app_opens
         FROM "map_user"
          GROUP BY "District","State"
          ORDER BY total_app_opens DESC
          limit 10;"""
        df = pd.read_sql_query(query, engine)
        st.title("2.Total App Opens by State (Stacked by District")
        stacked_chart = alt.Chart(df).mark_bar().encode(
        x="State",
        y="total_app_opens",
        color="District",
         tooltip=["State", "District", "total_app_opens"]
         ).properties(
         width=700,
         height=500,
         title="Total App Opens by State (Stacked by District)"
          )

        st.altair_chart(stacked_chart, width="stretch")
        query = """
        SELECT "District", "Year", "Quarter", SUM("registeredUsers") AS total_registered
        FROM "map_user"
        GROUP BY "District", "Year", "Quarter"
        ORDER BY total_registered DESC
        LIMIT 10;
        """

        df = pd.read_sql_query(query, engine)

        st.title("3.Top 10 District-Year-Quarter by Registered Users")

        stacked_bar = alt.Chart(df).mark_bar().encode(
         x=alt.X("District:N", title="District"),
          y=alt.Y("total_registered:Q", title="Total Registered Users"),
          color=alt.Color("Quarter:N", title="Quarter"),
         tooltip=["District", "Year", "Quarter", "total_registered"]
         ).properties(
           width=800,
         height=500,
          title="Quarterly Contribution in Top 10 District-Year-Quarter Combinations"
         )

        st.altair_chart(stacked_bar, width="stretch")



        query = """
        SELECT "State", "Year", SUM("registeredUsers") AS yearly_users
        FROM "map_user"
        GROUP BY "State", "Year"
         ORDER BY "State", "Year";
         """

        df = pd.read_sql_query(query, engine)
        
        st.title("4.Yearly Registered Users")

# Histogram of yearly_users
        hist = alt.Chart(df).mark_bar(opacity=0.7, color="steelblue").encode(
        alt.X("yearly_users:Q", bin=alt.Bin(maxbins=30)),  # bin into ranges
         y='count()',
        tooltip=['count()']
         ).properties(
         width=800,
        height=500,
        title="Distribution of Yearly Registered Users"
         )

        st.altair_chart(hist, width="stretch")


        query = """SELECT "District", SUM("appOpens") AS total_app_opens
          FROM "map_user"
           GROUP BY "District"
           ORDER BY total_app_opens DESC
            limit 10;"""
        df = pd.read_sql_query(query, engine)
        st.title("5.Top 10 Districts by App Opens")
        bar_chart = alt.Chart(df).mark_bar(color="steelblue").encode(
        x=alt.X("total_app_opens:Q", title="Total App Opens"),
        y=alt.Y("District:N", sort="-x", title="District"),
        tooltip=["District", "total_app_opens"]
         ).properties(
          width=800,
           height=500,
         title="Top 10 Districts by App Opens"
           )

        st.altair_chart(bar_chart, width="stretch")

