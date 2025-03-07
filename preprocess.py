from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[['transportation_mode']]).toarray()

# Convert to DataFrame and merge with original data
df_encoded = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['transportation_mode']))
df = pd.concat([df, df_encoded], axis=1).drop(columns=['transportation_mode'])
