from typing import Tuple, List, TypeVar
import requests
from pandas_gbq import read_gbq
from pandas import cut
from pandas import DataFrame
import numpy as np
from shapely import wkt
from libpysal import weights
import esda
import splot
from splot.esda import moran_scatterplot, plot_moran, lisa_cluster
from ipywidgets.embed import embed_minimal_html
import gmaps
from googlemaps import Client
from typing import Tuple, List
from multiprocessing import Pool
from .places import places
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PowerTransformer
from sklearn.decomposition import PCA, NMF, KernelPCA
from sklearn.manifold import TSNE, Isomap, SpectralEmbedding
from .geo_queries import query


T = TypeVar('T', int, float)

def getCentre(polygon) -> Tuple[float]:
    ''' Private member function that returns the centre from a group of
    coordinates

    :param polygon: a wkt geometry type of polygon POLYGON (lat lon, ...)
    :returns tuple: (lat, lon) centres
    '''

    i = 0
    lat = 0
    lon = 0
    for pt in list(polygon.exterior.coords):
        lat += pt[0]
        lon += pt[1]
        i += 1
    return (lat/i, lon/i)

def count_places(coords, api_key, radius=200) -> List[int]:
    '''
    Count the number of places given a radius
    '''
    api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&key={}"
    res = []
    places = requests.get(api_url.format(coords[0], coords[1], radius, api_key)).json()
    res.append(len(places['results']))

    return res


def POI(lat: float, lon: float, api_key, radius=200):
    '''
    return the POIs
    :param lat: latitude
    :param lon: longitude
    :param radius: radius of entry
    :param api_key: the api key, it is needed
    :return: dataframe of places
    '''

    def get_dist_time(d):
        if d['status'] == 'OK':
            return d['distance']['value'], d['duration']['value']
        else:
            return -99, -99

    gmap = Client(api_key)

    x = list()

    for place in places:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}".format(
            lat, lon, radius, place, api_key)
        res = requests.get(url).json()

        columns = places.copy()
        columns.append('distance_walking')
        columns.append('distance_bike')
        columns.append('distance_car')
        columns.append('distance_transit')
        columns.append('time_walking')
        columns.append('time_bike')
        columns.append('time_car')
        columns.append('time_transit')

        for idx, i in enumerate(res['results']):
            insert = {}
            lat_, lon_ = i['geometry']['location']['lat'], i['geometry']['location']['lng']
            insert[place] = [lat_, lon_]
            insert['name'] = i['name']

            dist_walking = \
            gmap.distance_matrix('{},{}'.format(lat, lon), '{},{}'.format(lat_, lon_), mode='walking')['rows'][0][
                'elements'][0]
            dist_car = \
            gmap.distance_matrix('{},{}'.format(lat, lon), '{},{}'.format(lat_, lon_), mode='driving')['rows'][0][
                'elements'][0]
            dist_bike = \
            gmap.distance_matrix('{},{}'.format(lat, lon), '{},{}'.format(lat_, lon_), mode='bicycling')['rows'][0][
                'elements'][0]
            dist_transit = \
            gmap.distance_matrix('{},{}'.format(lat, lon), '{},{}'.format(lat_, lon_), mode='transit')['rows'][0][
                'elements'][0]

            insert['distance_walking'], insert['time_walking'] = get_dist_time(dist_walking)
            insert['distance_car'], insert['time_car'] = get_dist_time(dist_car)
            insert['distance_bike'], insert['time_bike'] = get_dist_time(dist_bike)
            insert['distance_transit'], insert['time_transit'] = get_dist_time(dist_transit)

            x.append(insert)

    return DataFrame(x)

    # returns a list, and cycle through the list: .distance_matrix(lat, lon)
    # for i, j in zip(lat_lat, lon_lon):
    #   calculate distance(lat lon, i, j)
    #   append result

    # organise the dataframe
    # rows = the number of offers found
    # columns = distance, time, name of place,


    # return DataFrame(res, columns=columns)

#
# def write_to_db(index: List[T], location: str,  geometry, score: List[T], colors: List[T], dbname: str, port: int) -> None:
#
#     locale = np.array([location] * len(index))
#
#     insert_data = np.array([locale, index, geometry, score, colors]).T
#
#     try:
#         conn = connect(host='localhost', user='postgres', password='Prea2020',
#                                 port=port)  # change port when in use not hard
#         conn.autocommit = True
#     except:
#         print("I am unable to connect to the database")
#
#     cursor = conn.cursor()
#
#     try:
#         query = "CREATE TABLE {} (location, index, polygon, score)"
#     insert_stmt = "INSERT INTO {} (location, index, polygon, score, rank) VALUES (%s, %s, ST_GeomFromText(%s), %s, %s);".format(dbname)
#
#
#     psycopg2.extras.execute_batch(cursor, insert_stmt, insert_data)

def read_mapping_data(location):
    ''' Reads the latest features for the Lagekarte data
    :param location: string, a location in Germany
    :returns: pandas DataFrame
    '''
    print("Collecting data. please wait...")
    return read_gbq(query=query.format(location), project_id='mercury-262613', use_bqstorage_api=False)

def getCoords(polygon) -> List[Tuple]:
    '''
    private method turns score into colors in quantiles
    :param polygon: Polygon object from wkt.loads
    :return: None
    '''
    coords = list()
    for pt in list(polygon.exterior.coords):
        coords.append(pt)
    return coords

def plot_gmap(geometry, colors, name, api_key):
    '''
    store the html file of a google map with scores as colors
        :param: api_key
            the API key set for google maps [str]
    :param api_key:
    :return: html save file
    '''

    gmaps.configure(api_key)

    fig = gmaps.figure(center=(52, 13.5), zoom_level=8, layout={'background-color': 'black'})

    # collect coordinates
    pool = Pool(3)
    coords = np.array(pool.map(getCoords, geometry))

    for polygon, color in zip(coords, colors):
        try:
            polygonToDraw = gmaps.Polygon(polygon,
                                          stroke_color=color, fill_color=color)
            drawPolygonElement = gmaps.drawing_layer(features=[polygonToDraw], show_controls=False)
            fig.add_layer(drawPolygonElement)
        except:
            pass

    # embed_minimal_html("{}.html".format(name), views=[fig])
    return fig

def getScore(data, priority=None):
    '''
    creates a score based off of the PCs of the data to a 1d array
    :param data: a pandas DataFrame object or NumPy array
    :param priority: a string as a column in the dataframe, choosing to prioritise
    :return score: a NumPy array of scores from the 1d projections
    '''
    # Cleaning and scoring functions

    def _clean(data):
        data = data.select_dtypes(['float', 'int'])
        sub_under = data[data.med_price.apply(np.log) < 5]
        sub_over = data[data.med_price.apply(np.log) > 5]

        # preprocessing under
        sub_under.loc[:, 'med_price'] = sub_under.med_price.apply(np.log)
        # sub_under.loc[:, 'counts'] = sub_under.counts.apply(np.log)
        sub_under.loc[:, 'kaufkraft'] = sub_under.kaufkraft.apply(np.log)
        # sub_under.loc[:, 'moveinout'] = sub_under.moveinout.apply(np.tanh)
        # sub_under.loc[:, 'movement'] = sub_under.movement.apply(np.log)


        # preprocessing over
        sub_over.loc[:, 'med_price'] = sub_over.med_price.apply(np.log)
        # sub_over.loc[:, 'counts'] = sub_over.counts.apply(np.log)
        sub_over.loc[:, 'kaufkraft'] = sub_over.kaufkraft.apply(np.log)
        # sub_over.loc[:, 'moveinout'] = sub_over.moveinout.apply(np.tanh)
        # sub_over.loc[:, 'movement'] = sub_over.movement.apply(np.log)

        cols = sub_over.columns
        # min max
        sub_under = StandardScaler().fit_transform(sub_under)
        sub_over = StandardScaler().fit_transform(sub_over)

        return DataFrame(np.vstack((sub_under, sub_over)), columns=cols)

    def sigmoid(x):
        return 1 / (1 + np.exp(-1 * x))

    numeric = _clean(data)
    return numeric.applymap(np.sign).sum(axis=1)

    # def _clean(data):
        # def rank_income(data):
        #     income_data = data[['income_9', 'income_9_15', 'income_15_26', 'income_26_36', 'income_36_50', 'income_50']]
        #
        #     income_score = []
        #     for _, row in income_data.iterrows():
        #         income_score.append(np.argmax(row))
        #
        #     data['income'] = income_score
        #     return data.drop(income_data.columns, axis=1)
        #
        # def rank_house(data):
        #     house_data = data[['rank0','rank1','rank2','rank3','rank4','rank5','rank6','rank7','rank8','rank9','rank10']]
        #
        #     house_score = []
        #     for _, row in house_data.iterrows():
        #         house_score.append(np.argmax(row))
        #
        #     data['house'] = house_score
        #     return data.drop(house_data.columns, axis=1)

        # def rank_living(data):
        #     house_data = data[['living1','living2']]
        #
        #     house_score = []
        #     for _, row in house_data.iterrows():
        #         house_score.append(np.argmax(row))
        #
        #     data['living'] = house_score
        #     return data.drop(house_data.columns, axis=1)

        # df = rank_income(data)
        # df = rank_house(data)
        # df = rank_living(data)
        #
        # return df

    # def _weighting(data, priority):
    #     if priority is not None and len(priority) > 1:
    #         return data[priority]
    #     elif priority is not None and len(priority) == 1:
    #         return data[[priority[0]]]
    #     return data

    # numeric = _clean(data).select_dtypes(['float', 'int'])
    # kauf = numeric.kaufkraft.values
    # num = DataFrame(PowerTransformer().fit_transform(numeric.drop('kaufkraft', axis=1)))
    # num['kaufkraft'] = kauf
    # num = DataFrame(MinMaxScaler().fit_transform(num), columns = numeric.columns)
    # score = NMF(n_components=1).fit_transform(_weighting(num, priority=priority)).flatten()
    # return score

def getColors(score: List[T]) -> List[Tuple]:
    '''
    Cuts the score into colors using the PREA colors
    :param score:
    :return:
    '''

    colors = cut(score, 5, labels=[(78, 66, 245), (66, 245, 78), (245, 242, 66), (245, 120, 66), (255, 0, 0)])

    return colors

def addGeometry(geometry):
    ''' Applies the geometry to a column. loads are necessary'''
    res = geometry.apply(wkt.loads)

    return res


def getWeights(matrix, how):
    '''
    Creates an adjacency matrix with the Queen transforming, i.e. all neighbours from point i to up, right left, down, diagonals
    :param matrix: data matrix with geometry column.
    :return: returns the weight object
    '''
    if how == 'rook':
        weight = weights.Rook.from_dataframe(matrix)
    elif how == 'queen':
        weight = weights.Queen.from_dataframe(matrix)
    weight.transform = "R"

    return weight

def fitLag(weight, score):
    '''
    return new score with weights
    :param weights:
    :param score:
    :return:
    '''
    return weights.lag_spatial(weight, score)

def transform(data):
    '''
    Transforms the data with a box cox transform
    :param data: the data
    :return: return the transformed data matrix
    '''
    from sklearn.preprocessing import PowerTransformer
    X = DataFrame(PowerTransformer().fit_transform(data.drop(['kz', 'coords'], axis=1)),
                     columns=data.drop(['coords', 'kz'], axis=1).columns)
    X['geometry'] = data.coords
    X['kz'] = data.kz

    return X
