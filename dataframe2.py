import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your Streamlit code
def main():
    st.title("Data Analysis Application")
    st.subheader("This is a simple application for dataset analysis")

    # Dropdown for selecting a predefined dataset
    dataset_options = ["Iris", "Titanic", "Tips", "Upload Custom Dataset"]
    dataset_name = st.selectbox("Choose a dataset", dataset_options)

    # Load and display dataset based on selection
    if dataset_name != "Upload Custom Dataset":
        if dataset_name == "Iris":
            dataset_name = "iris.csv"
        elif dataset_name == "Titanic":
            dataset_name = "titanic.csv"
        elif dataset_name == "Tips":
            dataset_name = "tips.csv"

        # Load the selected dataset
        try:
            df = pd.read_csv(dataset_name)
            st.write(f"Displaying {dataset_name} dataset:")
            st.write(df)
            st.write("Number of Rows", df.shape[0])
            st.write("Number of Columns", df.shape[1])
            st.write('Column names and data types ', df.dtypes)
            st.write("Summary Statistics ", df.describe())

            x_axis = st.selectbox("Select X-axis", df.columns)
            y_axis = st.selectbox("Select Y-axis", df.columns)
            plot_type = st.selectbox("Select Plot Type", ['line', 'scatter', 'bar', 'hist', 'box'])

            if plot_type == 'line':
                st.line_chart(df[[x_axis, y_axis]])
            elif plot_type == 'scatter':
                st.scatter_chart(df[[x_axis, y_axis]])
            elif plot_type == 'bar':
                st.bar_chart(df[[x_axis, y_axis]])
            elif plot_type == 'hist':
                plt.hist(df[x_axis], bins=20, alpha=0.7)
                st.pyplot()
            elif plot_type == 'box':
                df[[x_axis, y_axis]].plot(kind='box')
                st.pyplot()
            elif plot_type == 'kde':
                df[[x_axis, y_axis]].plot(kind='kde')
                st.pyplot()

            if df.isnull().sum().sum() > 0:
                st.write("Null values ", df.isnull().sum().sort_values(ascending=False))
            else:
                st.write("No Null values")

            st.subheader('Pairplot')
            hue_column = st.selectbox('Select a column to be used as hue', df.columns)
            st.pyplot(sns.pairplot(df, hue=hue_column, markers='o'))

        except Exception as e:
            st.error(f"Error reading the dataset: {e}")

    # Option to upload a custom dataset
    else:
        uploaded_file = st.file_uploader("Upload a custom dataset", type=["csv", "xlsx"])

        if uploaded_file is not None:
            if st.button("Load Custom Dataset"):
                try:
                    # Check the file extension and read accordingly
                    if uploaded_file.name.endswith(".csv"):
                        df = pd.read_csv(uploaded_file)
                    elif uploaded_file.name.endswith(".xlsx"):
                        df = pd.read_excel(uploaded_file)

                    st.write(f"Displaying uploaded dataset:")
                    st.write(df.head(5))  # Display first 5 rows

                except Exception as e:
                    st.error(f"Error reading the file: {e}")
        else:
            st.write("Please upload a CSV or Excel file.")


if __name__ == "__main__":
    main()
