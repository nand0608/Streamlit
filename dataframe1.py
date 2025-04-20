import streamlit as st
import pandas as pd


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
        df = pd.read_csv(dataset_name)
        st.write(f"Displaying {dataset_name} dataset:")
        st.write(df.head(5))

    # Option to upload a custom dataset
    else:
        uploaded_file = st.file_uploader("Upload a custom dataset", type=["csv", "xlsx"])

        if uploaded_file is not None:
            if st.button("Load Custom Dataset"):
                # Read the uploaded file into a dataframe
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
