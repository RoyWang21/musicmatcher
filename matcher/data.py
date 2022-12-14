# data.py for ETL process
import pandas as pd
import sklearn.preprocessing as skpp


def etl_data(args):
    """Extract, Load and Transform Data Pipeline
    Returns:
        pd.DataFrame: df_tracks contains meta info of tracks in library
        np.ndarray: Train_X contains numerical features for training model
    """
    # Load
    df_tracks = pd.read_csv("data/sample_tracks_from_fulllist.csv", index_col=0)
    df_item_features = pd.read_csv("data/extracted_track_list_marksample.csv")

    # Extract
    # select relevant columns
    df_tracks = df_tracks[args.read_cols]
    df_item_features = df_item_features[["id"] + args.numerical_cols]
    df_tracks = df_tracks.dropna(axis=0)

    # extract track id
    df_tracks["track_id"] = df_tracks.apply(lambda x: x["track_uri"].split(":")[-1], axis=1)
    # extract album id
    df_tracks["album_id"] = df_tracks.apply(lambda x: x["album_uri"].split(":")[-1], axis=1)
    # extract artist id
    df_tracks["artist_id"] = df_tracks.apply(lambda x: x["artist_uri"].split(":")[-1], axis=1)

    # Transform
    # merge datasets
    df_tracks = pd.merge(
        df_tracks, df_item_features, how="inner", left_on="track_id", right_on="id"
    )
    #    df_tracks = df_tracks.drop(["album_uri", "artist_uri", "track_uri", "id"], axis=1)
    df_tracks = df_tracks.drop_duplicates("track_id").reset_index(drop=True)
    train_X = df_tracks[args.numerical_cols].values

    # scaling
    scaler = skpp.MinMaxScaler()
    train_X = scaler.fit_transform(train_X)

    # convert str to all lower cases
    df_tracks["track_name"] = df_tracks["track_name"].str.lower()
    df_tracks["artist_name"] = df_tracks["artist_name"].str.lower()
    return df_tracks[args.identity_cols], train_X
