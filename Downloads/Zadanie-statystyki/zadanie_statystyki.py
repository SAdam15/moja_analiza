{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "da8b325a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Filmy:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>budget</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>genre_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>237000000</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>300000000</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>285</td>\n",
       "      <td>en</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>139.082615</td>\n",
       "      <td>2007-05-19</td>\n",
       "      <td>961000000</td>\n",
       "      <td>169.0</td>\n",
       "      <td>Released</td>\n",
       "      <td>At the end of the world, the adventure begins.</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>6.9</td>\n",
       "      <td>4500</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>245000000</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>206647</td>\n",
       "      <td>en</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>107.376788</td>\n",
       "      <td>2015-10-26</td>\n",
       "      <td>880674609</td>\n",
       "      <td>148.0</td>\n",
       "      <td>Released</td>\n",
       "      <td>A Plan No One Escapes</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>6.3</td>\n",
       "      <td>4466</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>250000000</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>49026</td>\n",
       "      <td>en</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>Following the death of District Attorney Harve...</td>\n",
       "      <td>112.312950</td>\n",
       "      <td>2012-07-16</td>\n",
       "      <td>1084939099</td>\n",
       "      <td>165.0</td>\n",
       "      <td>Released</td>\n",
       "      <td>The Legend Ends</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>7.6</td>\n",
       "      <td>9106</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>260000000</td>\n",
       "      <td>http://movies.disney.com/john-carter</td>\n",
       "      <td>49529</td>\n",
       "      <td>en</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>John Carter is a war-weary, former military ca...</td>\n",
       "      <td>43.926995</td>\n",
       "      <td>2012-03-07</td>\n",
       "      <td>284139100</td>\n",
       "      <td>132.0</td>\n",
       "      <td>Released</td>\n",
       "      <td>Lost in our world, found in another.</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>6.1</td>\n",
       "      <td>2124</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0     budget                                      homepage  \\\n",
       "0           0  237000000                   http://www.avatarmovie.com/   \n",
       "1           1  300000000  http://disney.go.com/disneypictures/pirates/   \n",
       "2           2  245000000   http://www.sonypictures.com/movies/spectre/   \n",
       "3           3  250000000            http://www.thedarkknightrises.com/   \n",
       "4           4  260000000          http://movies.disney.com/john-carter   \n",
       "\n",
       "       id original_language                            original_title  \\\n",
       "0   19995                en                                    Avatar   \n",
       "1     285                en  Pirates of the Caribbean: At World's End   \n",
       "2  206647                en                                   Spectre   \n",
       "3   49026                en                     The Dark Knight Rises   \n",
       "4   49529                en                               John Carter   \n",
       "\n",
       "                                            overview  popularity release_date  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...  150.437577   2009-12-10   \n",
       "1  Captain Barbossa, long believed to be dead, ha...  139.082615   2007-05-19   \n",
       "2  A cryptic message from Bond’s past sends him o...  107.376788   2015-10-26   \n",
       "3  Following the death of District Attorney Harve...  112.312950   2012-07-16   \n",
       "4  John Carter is a war-weary, former military ca...   43.926995   2012-03-07   \n",
       "\n",
       "      revenue  runtime    status  \\\n",
       "0  2787965087    162.0  Released   \n",
       "1   961000000    169.0  Released   \n",
       "2   880674609    148.0  Released   \n",
       "3  1084939099    165.0  Released   \n",
       "4   284139100    132.0  Released   \n",
       "\n",
       "                                          tagline  \\\n",
       "0                     Enter the World of Pandora.   \n",
       "1  At the end of the world, the adventure begins.   \n",
       "2                           A Plan No One Escapes   \n",
       "3                                 The Legend Ends   \n",
       "4            Lost in our world, found in another.   \n",
       "\n",
       "                                      title  vote_average  vote_count  \\\n",
       "0                                    Avatar           7.2       11800   \n",
       "1  Pirates of the Caribbean: At World's End           6.9        4500   \n",
       "2                                   Spectre           6.3        4466   \n",
       "3                     The Dark Knight Rises           7.6        9106   \n",
       "4                               John Carter           6.1        2124   \n",
       "\n",
       "   genre_id  \n",
       "0      28.0  \n",
       "1      12.0  \n",
       "2      28.0  \n",
       "3      28.0  \n",
       "4      28.0  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gatunki:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>28.0</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12.0</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14.0</td>\n",
       "      <td>Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16.0</td>\n",
       "      <td>Animation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>878.0</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0           genres\n",
       "0        28.0           Action\n",
       "1        12.0        Adventure\n",
       "2        14.0          Fantasy\n",
       "3        16.0        Animation\n",
       "4       878.0  Science Fiction"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Ścieżki do plików\n",
    "movies_path = \"C:/Users/abero/Downloads/tmdb_movies.csv\"\n",
    "genres_path = \"C:/Users/abero/Downloads/tmdb_genres.csv\"\n",
    "\n",
    "# Wczytanie danych\n",
    "movies = pd.read_csv(movies_path)\n",
    "genres = pd.read_csv(genres_path)\n",
    "\n",
    "# Podgląd danych\n",
    "print(\"Filmy:\")\n",
    "display(movies.head())\n",
    "\n",
    "print(\"Gatunki:\")\n",
    "display(genres.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b2b9ddd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1881</th>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>8.5</td>\n",
       "      <td>8205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3337</th>\n",
       "      <td>The Godfather</td>\n",
       "      <td>8.4</td>\n",
       "      <td>5893</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>662</th>\n",
       "      <td>Fight Club</td>\n",
       "      <td>8.3</td>\n",
       "      <td>9413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2731</th>\n",
       "      <td>The Godfather: Part II</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3338</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3232</th>\n",
       "      <td>Pulp Fiction</td>\n",
       "      <td>8.3</td>\n",
       "      <td>8428</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2294</th>\n",
       "      <td>Spirited Away</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3840</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1818</th>\n",
       "      <td>Schindler's List</td>\n",
       "      <td>8.3</td>\n",
       "      <td>4329</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3865</th>\n",
       "      <td>Whiplash</td>\n",
       "      <td>8.3</td>\n",
       "      <td>4254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1663</th>\n",
       "      <td>Once Upon a Time in America</td>\n",
       "      <td>8.2</td>\n",
       "      <td>1069</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1847</th>\n",
       "      <td>GoodFellas</td>\n",
       "      <td>8.2</td>\n",
       "      <td>3128</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            title  vote_average  vote_count\n",
       "1881     The Shawshank Redemption           8.5        8205\n",
       "3337                The Godfather           8.4        5893\n",
       "662                    Fight Club           8.3        9413\n",
       "2731       The Godfather: Part II           8.3        3338\n",
       "3232                 Pulp Fiction           8.3        8428\n",
       "2294                Spirited Away           8.3        3840\n",
       "1818             Schindler's List           8.3        4329\n",
       "3865                     Whiplash           8.3        4254\n",
       "1663  Once Upon a Time in America           8.2        1069\n",
       "1847                   GoodFellas           8.2        3128"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Obliczenie 3. kwartylu dla vote_count\n",
    "q3_vote_count = movies[\"vote_count\"].quantile(0.75)\n",
    "\n",
    "# Filtrowanie filmów z liczba głosów > Q3\n",
    "popular_movies = movies[movies[\"vote_count\"] > q3_vote_count]\n",
    "\n",
    "# Sortowanie według najwyższej oceny\n",
    "top_10_movies = popular_movies.sort_values(by=\"vote_average\", ascending=False).head(10)\n",
    "\n",
    "# Wyświetlenie wybranych kolumn\n",
    "top_10_movies[[\"title\", \"vote_average\", \"vote_count\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ab5ade7b",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'release_year'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3805\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3804\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m3805\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_engine\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcasted_key\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   3806\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[36mFile \u001b[39m\u001b[32mindex.pyx:167\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mindex.pyx:196\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas\\\\_libs\\\\hashtable_class_helper.pxi:7081\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas\\\\_libs\\\\hashtable_class_helper.pxi:7089\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[31mKeyError\u001b[39m: 'release_year'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mmatplotlib\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mpyplot\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mplt\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# Filtrowanie lat 2010–2016 (włącznie)\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m filtered = movies[(\u001b[43mmovies\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mrelease_year\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m >= \u001b[32m2010\u001b[39m) & (movies[\u001b[33m\"\u001b[39m\u001b[33mrelease_year\u001b[39m\u001b[33m\"\u001b[39m] <= \u001b[32m2016\u001b[39m)]\n\u001b[32m      6\u001b[39m \u001b[38;5;66;03m# Grupowanie i obliczanie średniego budżetu i przychodu\u001b[39;00m\n\u001b[32m      7\u001b[39m grouped = filtered.groupby(\u001b[33m\"\u001b[39m\u001b[33mrelease_year\u001b[39m\u001b[33m\"\u001b[39m)[[\u001b[33m\"\u001b[39m\u001b[33mrevenue\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mbudget\u001b[39m\u001b[33m\"\u001b[39m]].mean().reset_index()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\frame.py:4102\u001b[39m, in \u001b[36mDataFrame.__getitem__\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   4100\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m.columns.nlevels > \u001b[32m1\u001b[39m:\n\u001b[32m   4101\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m._getitem_multilevel(key)\n\u001b[32m-> \u001b[39m\u001b[32m4102\u001b[39m indexer = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   4103\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m is_integer(indexer):\n\u001b[32m   4104\u001b[39m     indexer = [indexer]\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3812\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3807\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(casted_key, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;129;01mor\u001b[39;00m (\n\u001b[32m   3808\u001b[39m         \u001b[38;5;28misinstance\u001b[39m(casted_key, abc.Iterable)\n\u001b[32m   3809\u001b[39m         \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28many\u001b[39m(\u001b[38;5;28misinstance\u001b[39m(x, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;28;01mfor\u001b[39;00m x \u001b[38;5;129;01min\u001b[39;00m casted_key)\n\u001b[32m   3810\u001b[39m     ):\n\u001b[32m   3811\u001b[39m         \u001b[38;5;28;01mraise\u001b[39;00m InvalidIndexError(key)\n\u001b[32m-> \u001b[39m\u001b[32m3812\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01merr\u001b[39;00m\n\u001b[32m   3813\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m:\n\u001b[32m   3814\u001b[39m     \u001b[38;5;66;03m# If we have a listlike key, _check_indexing_error will raise\u001b[39;00m\n\u001b[32m   3815\u001b[39m     \u001b[38;5;66;03m#  InvalidIndexError. Otherwise we fall through and re-raise\u001b[39;00m\n\u001b[32m   3816\u001b[39m     \u001b[38;5;66;03m#  the TypeError.\u001b[39;00m\n\u001b[32m   3817\u001b[39m     \u001b[38;5;28mself\u001b[39m._check_indexing_error(key)\n",
      "\u001b[31mKeyError\u001b[39m: 'release_year'"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Filtrowanie lat 2010–2016 \n",
    "filtered = movies[(movies[\"release_year\"] >= 2010) & (movies[\"release_year\"] <= 2016)]\n",
    "\n",
    "# Grupowanie i obliczanie średniego budżetu i przychodu\n",
    "grouped = filtered.groupby(\"release_year\")[[\"revenue\", \"budget\"]].mean().reset_index()\n",
    "\n",
    "# Tworzenie wykersu\n",
    "fig, ax1 = plt.subplots(figsize=(10, 6))\n",
    "\n",
    "# Wykres kolumnowy: revenue\n",
    "ax1.bar(grouped[\"release_year\"], grouped[\"revenue\"], color=\"skyblue\", label=\"Średni przychód\")\n",
    "ax1.set_ylabel(\"Średni przychód (USD)\")\n",
    "ax1.set_xlabel(\"Rok wydania\")\n",
    "ax1.set_xticks(grouped[\"release_year\"])\n",
    "ax1.tick_params(axis='y')\n",
    "ax1.set_title(\"Średni przychód i budżet filmów (2010–2016)\")\n",
    "\n",
    "# Wykres liniowy\n",
    "ax2 = ax1.twinx()\n",
    "ax2.plot(grouped[\"release_year\"], grouped[\"budget\"], color=\"darkblue\", linewidth=2, marker=\"o\", label=\"Średni budżet\")\n",
    "ax2.set_ylabel(\"Średni budżet (USD)\")\n",
    "ax2.tick_params(axis='y')\n",
    "\n",
    "# Legenda poza wykresem\n",
    "fig.legend(loc=\"upper right\", bbox_to_anchor=(1.15, 1.0))\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "eb4c3a01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Unnamed: 0', 'budget', 'homepage', 'id', 'original_language',\n",
       "       'original_title', 'overview', 'popularity', 'release_date', 'revenue',\n",
       "       'runtime', 'status', 'tagline', 'title', 'vote_average', 'vote_count',\n",
       "       'genre_id'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b9d58e90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    2009-12-10\n",
       "1    2007-05-19\n",
       "2    2015-10-26\n",
       "3    2012-07-16\n",
       "4    2012-03-07\n",
       "Name: release_date, dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"release_date\"].head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b02ea254",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Konwersja kolumny na typ datetime\n",
    "movies[\"release_date\"] = pd.to_datetime(movies[\"release_date\"], errors=\"coerce\")\n",
    "\n",
    "# Wyciągnięcie roku do nowej kolumny\n",
    "movies[\"release_year\"] = movies[\"release_date\"].dt.year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4173d67e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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gGf179HD+/79G1s9HHiJyMhIM+tWaQQHB0urVq3Meo8ePWT58uUybdo0eeONN07Y95FHHjHlWzfffLO5fMopp5gSsFtvvVUeeugh05S5JLVq1Sp0LquJDFp+Fh4ebkrFAJ8J+OiLX0u39M2mNY1XX321PPzww443FwAAAADPdeBApqxde8Csd+9eT2rVCrV6SIDk5+ebShNXMjMzTwjq2NuNlKYKRad0d6b3VbduXenTp48JBgE+E/BxphFTnSrvyiuvlMWLF1fGXQIAAACw0C+/UM4Fa2mp13nnnSdNmzY1mTY67bqWbc2bN89cP3z4cFNqZe8BpLN66fTr3bp1M0GarVu3mqwf3V6aPrNaLgZ4k3IHfJo1a1boTaMNnHV6vKJT5wEAAADw7OnYBwxgOnZUv6SkJBPU2bt3r2nu3LlzZxPsGTJkiLl+x44dhTJ6tOJES7L0/927d5vsHD0/1encSyslJUXefvtt2bhxo7msDaJvuOEGqV27dhU8QsANAz46Jd577713QpRUaytXr15tZuoCAAAA4LkWLCjI8AkM9JczzqB/D6qfBl5Kotk+zgIDA2XChAlmKQ+tVtEAkQaXevbsabZpw2ad+eubb76R/v37l+t+AY8K+Gig5+yzzzZRz5o1axa6LjQ01GT/AAAAAPBMe/aky6ZNB816r171JTIy2OohAVVu1KhRpjfta6+95khu0GSHkSNHmut0injAJ6Zl79SpkyQkJFTuaAAAAABYbuHC4+Vc9O+Br9CeP/fee2+hShZdHzNmjLkO8JmAzxNPPCH33XefzJ0719RUpqamFloAAAAAeH7/HgI+8BXdu3d39O5xptu6dOliyZgAS5o2n3/++eb/iy++2DTGstPp7vSypr4BAAAA8DwLFxb07wkODpC+fRtYPRygyqxdu9axftddd8no0aNNNs+pp55qtunERK+88opMnjzZwlEC1RzwWbhwYXlvCgAAAMBNbdt2WBITD5v1005rKGFhQVYPCagyXbt2NQkLmrhg98ADD5yw37XXXmv6+wA+EfA588wzK3ckAAAAACxH/x74ksTERKuHALhfwEelpKSYqfLsdY4dOnSQG264QWrXrl1Z4wMAAABgwXTsasCAJpaOBahqzDANb1bups2LFy+W5s2by4svvmgCP7roeosWLcx1AAAAADyLlrXYGzaHhwdK79707wEAn8vwGTVqlKlhfO211xzT1mmj5pEjR5rr1q1bV5njBAAAAFDFtmxJkT170s16v36NTdNmAICPZfho5/J7773XEexRuj5mzBhzHQAAAADPnY6dci4A8GzlDvh0797d0bvHmW7r0qVLRccFAAAAwMKADw2bAcBHS7ruuusuGT16tMnmOfXUU822ZcuWySuvvCKTJ0+WtWvXOvbt3Llz5YwWAAAAQJXIz7fJokUFDZujooKlW7d6Vg8JAGBFwOeaa64x/z/wwAMur/Pz8zNN3/R/7e0DAAAAwH2tX58sBw4cMetnntlEAgPLXQwAeAydYXrz5s0SExMjtWrVMuevxTl48GC1jg2wLOCTmJhY4R8OAAAAwD1QzgVfNHXqVImMjDTrL7zwgtXDAdwj4NOsWbPKHQkAAAAAyyxcWFDOpWjYDF8xYsQIl+uATwd8AAAAAHiHvLx8R/+eOnXC5JRT6lo9JMAS+fn5pk9tUlKSWXfWv39/y8YFlAcBHwAAAMDHrVmTJIcPZzmye/z9i+9jAngrnYTo2muvle3bt5t+tM7oTQtPRMAHAAAA8HHO/Xso54Kvuu2226Rnz57y7bffSoMGDUps4Ax4AgI+AAAAgI+jYTMgsmXLFvn888+lVatWVg8FqBTMtQgAAAD4sLycfFmyZLdZb9CghrRtW9vqIQGW6NOnj+nfA/hkhk/t2rVl8+bNEhMTI7Vq1Soxxe3gwYOVMT4AAAAAVWjXhmTJyMgx6wMGNKWMBT7rzjvvlHvvvVf27dsnp5xyigQFBRW6vnPnzpaNDajygM/UqVMlMjLSrL/wwgvl+oEAAAAA3Ef88r2Odcq54Msuv/xy8/+NN97o2KYBUG3gTNNmeH3AZ8SIES7XAQAAAHimhOX7HOs0bIYvS0xMtHoIgPs0bc7Pzzc1jklJSWbdWf/+/ct8f6+88oo888wzJoWuS5cu8tJLL0nv3r2L3f/QoUPy0EMPyezZs00JWbNmzUzm0fnnn1+uxwMAAAD4kpysXNn+136z3qxZlLRoEW31kADL6Pkk4E3KHfBZtmyZXHvttbJ9+3aT4uasPOlun3zyiYwZM0Zef/110yxLAzfnnHOObNq0SWJjY0/YPzs7W4YMGWKu007qjRo1MmOpWbNmeR8SAAAA4FN2rD0gudn5jnIu+vfA13z99del3vfiiy+u0rEAbhPwue2226Rnz57y7bffSoMGDSr84fD888/LLbfcIjfccIO5rIEfve8ZM2bI2LFjT9hft2tWz++//+5optW8efMKjQEAAADwJQkrKOeCbxs6dGihy/aePc6X7ejhA5+Zln3Lli3y1FNPSfv27U1WTXR0dKGlLDRbZ+XKlTJ48ODjA/P3N5eXLl1abCS2b9++MmrUKKlXr5506tTJjIc3IQAAAFD2hs06Qxfga7Q1iX358ccfpWvXrvL999+b9iG6fPfdd9K9e3f54YcfrB4qUH0ZPlp2pf17WrVqJRWVnJxsAjUauHGml//55x+Xt0lISJAFCxbIsGHDzJtQxzJy5EjJycmRCRMmuLxNVlaWWezS0tIqPHYAAADAE2UfyZGdfx8w623a1JLGjQtm4wV81d13320qTc444wzHNm0zEh4eLrfeeqts3LjR0vEB1RbwufPOO+Xee+81DZZPOeUUR1mVXefOnaUqaQRW+/e8+eabEhAQID169JDdu3ebps/FBXwmTZokjz32WJWOCwAAAPAE21YnSX5uQekK2T2ASHx8vMuesFrBsm3bNkvGBFgS8Ln88svN/zfeeOMJ9Y5lbdocExNjgjb79xfMEGCnl+vXr+/yNto3SINMejs7LS/TAJSWiAUHB59wm3HjxpnG0HYaIOrQoUOpxwkAAAB4YznXwIH07wF69eplzhc/+OADR/WJnpPef//9Jc4eDXhdwCcxMbHSBqHBGc3QmT9/vqNplmbw6OU77rjD5W1OP/10mTlzptlP+/2ozZs3m0CQq2CPCgkJMYtdampqpT0GAAAAwFMbNp91FgEfQCcGuvTSS6Vp06bSpEnBe2Lnzp3SunVr+fLLL60eHlB9AZ9mzZpJZdJI6ogRI8zMXxo91WnZMzIyHLN2DR8+3Ey9rmVZ6vbbb5eXX35ZRo8ebcrL7E2k77rrrkodFwAAAOBtjqRlye6N/5r1eq1qSmxsDauHBFhO+9OuXbtWfvrpJ0cvWa0i0cmEKjorNeD2AR+dGau0Lr744jIN5Oqrr5YDBw7I+PHjTVmWdkfXTuj2VLodO3Y4MnmURlznzZsn99xzj+kXpMEgDf48+OCDZfq5AAAAgK9JXLVfbPkF/Xta9mpg9XAAt6GBnbPPPlv69+9vqkMI9MBnAj72cquiPXucL9uVZ3p0Ld8qroRr0aJFJ2zTadmXLVtW5p8DAAAA+LKE5cfLueJ6uu6ZCfgabRfy5JNPmpm6tHePtgyJi4uTRx55RJo3by433XST1UMEyuR4ykwp3wD25ccffzRZON9//70cOnTILDo9evfu3U1mDgAAAAD3btis39fG9SDgA6gnnnhC3n33XZkyZUqhvrCdOnWSt956y9KxAdXaw+fuu+82kc8zzjjDse2cc86R8PBwufXWW2Xjxo3lvWsAAAAAVSQ95ajs25Ji1hu2qyNhUccnNQF82fvvvy9vvvmmDBo0SG677TbH9i5dujh6+gBem+HjLD4+XmrWrHnC9ujoaNm2bVtFxwUAAACgCiSupJwLcGX37t2mcXNRWuGSk5NjyZgASwI+vXr1MjNraW2jna7ff//9ZpYtAAAAAO5bzqVa9qZhM2DXoUMHWbJkyQnbP//8c+nWrZslYwIsKemaMWOGXHrppdK0aVMzY5bauXOntG7dWr788ssKDQoAAABA1TZs9g/0k+ZdC2bEBSBmxugRI0aYTB/N6pk9e7Zs2rTJlHrNnTvX6uEB1Rfw0VS3tWvXyk8//eSoZ2zfvr0MHjyYqesAAAAAN5R6IFMObDts1ht3iJGQGkFWDwlwG5dccol888038vjjj0uNGjVMAEgnJdJtQ4YMsXp4QPUFfJQGds4++2zp37+/hISEEOgBAAAAPKWcqxflXIBdbm6uPPXUU3LjjTeapAbAp3v4aIrbxIkTpVGjRhIRESGJiYlm+yOPPCJvv/12ZY4RAAAAQCVIWHG8YTMBH+C4wMBAMx27Bn4A8fWAzxNPPCHvvvuueVMEBwc7tnfq1EneeuutyhofAAAAgErO8AkI8pemnetaPRzAreh07L/88ovVwwCsL+nSxlVvvvmmeVPcdtttju1dunRx9PQBAAAA4B5S9qRJyu50s96sS6wEhVaouwPgdc477zwZO3asrFu3Tnr06GH6+Di7+OKLLRsbUB7l/iuvncu1cbOrUq+cnJzy3i0AAACAKhB/bHYuFdezvqVjAdzRyJEjzf/PP//8Cddpv9q8vDwLRgVYUNLVoUMHWbJkyQnbP//8c+nWrVsFhgQAAACgstGwGSiZJi8UtxDsgU9l+OgUdSNGjDCZPvoGmD17tmzatMmUes2dO7dyRwkAAACg3Gw2myQcy/DRUq7GnWKsHhIAwF0zfC655BL55ptv5Oeffza1jRoA2rhxo9k2ZMiQyh0lAAAAgHJL3pEqqQcyzXrzrrESGBRg9ZAAt7F06dITkhY0kaFFixYSGxsrt956q2RlZVk2PqBaAz46Vd3jjz9u3gA//fSTJCUlSWZmpvz6669y9tlnl3swAAAAACpfgnM5V2/KuQBnem67fv16x2Vt2nzTTTfJ4MGDTRNnTWqYNGmSpWMEqi3gExgYaKZj18APAAAAAA9q2Ez/Hvi4qVOnyldffeW4vGbNGjP7tN2sWbOkT58+Mn36dBkzZoy8+OKL8umnn1o0WsCCki59Q/zyyy8V+NEAAAAAqlp+vk0SVhQEfEIigqRh29pWDwmwlFalPPLII/Lxxx+byykpKVKvXj3H9Xqeq1O02/Xq1Ut27txpyVgBSwI++gbQ9Lb77rvPvFG+/vrrQgsAAAAA6yXFH5KMlKNmPa57fQkILPcpAFCtXnvtNencubNERUWZpW/fvvL999+XeJtDhw7JqFGjpEGDBhISEiJt2rSR7777rtA+HTt2lBUrVpiZp5UGexITE816dna2rFq1Sk499VTH/mlpaRIUFFQljxFwy1m6Ro4caf5//vnnT7jOz8+PaesAAAAANxC/4nj/nrhe9S0dC1AWjRs3lsmTJ0vr1q3NTHPvvfeemTxo9erVJmhTlAZrdAIhbbT8+eefS6NGjWT79u1Ss2bNE/YNDg6WLl26mPXzzz/fJDM8/fTT8uWXX0p4eLj069fPse/atWulZcuWVfxoATcK+OhU7AAAAAA8qGEz/XvgQS666KJCl5988kmT9bNs2TKXAZ8ZM2bIwYMH5ffff3dk5DRv3vykP2fixIly2WWXyZlnnikREREmsKQBIef7ZXIi+FTABwAAAIB7y8/Ld/TvCa8ZIvVa1bJ6SIApkUpNTXVc1tIrXUqiFSSfffaZZGRkmNIuV7S1iF6nJV3alLlu3bpy7bXXyoMPPigBAQHF3ndMTIwsXrxYDh8+bAI+RffVn6vbAU9T5gLepUuXyty5cwtte//9980U7Zo6d+utt0pWVlZljhEAAABAOezddFCOpueY9bge9cXf38/qIQGmd050dLRjKWnKc50iXYMtGhC67bbbZM6cOY7eO0UlJCSYUi4NDmnfHm3M/Nxzz8kTTzxRqnHpWFwFhmrXrl0o4wfw2gyfxx9/XM466yy58MILHW/Am266Sa6//npp3769PPPMM9KwYUN59NFHq2K8AAAAAEqJ6djhjjZs2GD669iVlN3Ttm1bM226Zt9oMGfEiBFmFi1XQR9tO6JJCG+++aYJ3PTo0UN2795tzlEnTJhQZY8H8NiAz9SpUyUuLs40x1L6ZtMaR7tZs2ZJnz59ZPr06eZykyZNzJuJgA8AAABgrfhC/Xto2Az3EBkZaWbdKg3NrGnVqpVZ1wDO8uXLZdq0afLGG2+csK/OzKW9e5yzdDQpYd++faahM1k68DUnLenS5lSaCqdTr6uUlBQzbZ2dRld1ina7Xr16yc6dO6tqvAAAAABKIS8nX7at3m/WI2PCpG7zaKuHBFSYZvEU10Lk9NNPl61btxaaYGjz5s0mEESwB77opAEf7X6+YsUKR8qcBnsSExPNukZJV61aJaeeemqhBlz2jugAAAAArLFrQ7JkH8l1lHP5+dG/B55l3Lhxppnytm3bTCsRvbxo0SIZNmyYuX748OFmm93tt99uZukaPXq0CfR8++238tRTT5kmzoAvKlUPH42GdunSxayff/75MnbsWHn66aflyy+/lPDwcOnXr59j37Vr10rLli2rbsQAAAAAyjgdO+Vc8DxJSUkmqLN3717TULlz584yb948GTJkiLl+x44d4u9/PIdB24vo9ffcc4/ZV/sEafBHZ+kCfFGZmzZr/57LLrtMzjzzTNMt/b333iuUHjdjxgxTBgYAAADAPRo2t+xJw2Z4nrfffrvE6zXbpyidln3ZsmVVOCrAiwM+MTExJq1Ou6RrwKfotHWfffaZ2Q4AAADAGjlZubL9r4L+PTUb1JBajTg+BwBfU+aAj52m1LlSu3btiowHAAAAQAXtXHdAcrMLGte2pH8PAPikkzZtBgAAAOC55VxxlHMBgE8qd4YPAACofvl5BdMspyYfkaiYMGnerZ74B/D9DYDC4mnYDAA+j4APAAAe4u/522XuM3/I4aRMx7bo2HC58P4+0mlQM0vHBsB9ZB/JkZ1/HzDrdZpGSXS9GlYPCQBgAb4SBADAQ4I9Hz2wsFCwRx0+kGm26/UAoLatTpL8XJtZJ7sHAHwXAR8AADygjOubKX+IFJy/FXZs29xn/zD7AUDhci769wCAr6KkCwAAN5Jx6KgcSDwsSWY5JEkJh2TPPwclI+Vo8TeyiRzen2l6+9CcFUDCCueGzWT4AICvIuADAEA1s9lskpqU6QjqHHAEdw6XHNg5CW3kDMC3HU3Llt0b/zXr9VrVlIjaYVYPCQBgEQI+AABUES2xOrg7vXBQJ/GwWc/KyCn1/QSFBkjO0byT7qezdgHwbYmr9ost396/h4w/APBlBHwAAKig3Ow8Sd6e6ijBsgd1knccltzs0vfViagTKrEtapqlbotoidUlrqbUqBUiz1z4hWnQ7LKPj87WVS/cTNEOwLc59++hnAsAfBsBHwAASkmzco5n6RSUYOllzeKxf6NeGrUaRpiATr04e2BHgzzREhYVUuxtdOp1nY1L/I43anbWqEMd8Q9gLgbA19kDPn5+InE9CPgAgC8j4AMAQBHpKUdNpo4J6hxroKzr2hi5tPwD/SSmSZTUPRbM0Uwd/T+mWbQEh5X947fToGYybMoAmfvMHydMza42LNwpq7+Ll27ntyzzfQPwDtoDbN+WFLPeoG2dEoPIAADvR8AHAOCzjZN37kyTzb/vdirDOiRJ2w5L5qGsUt9PUGig1G1+rPyqRXRBgCcuWuo0jpKAoMrNuNGgT4ezmpjZuLRBs/bs2bs5ReY++6e5fvbjv5mAUpOOMZX6cwF4hoSVx2fnatmL7B4A8HUEfAAAXi03N1/i4w/Jxo3/ysaNB2XDBv3/X/lHpzovQ+PksKhgR5aOI2unRbRE148Qf3+ts6oeWrblPPV6ix71ZX98iiyfs8X0C/pwzAIZ9eGFElU3vNrGBMD9+ve07E3DZgDwdQR8AABe4ciRHNm0KeVYYOd4cGfLlhTJySl942QNlJi+OseCO/YAT0TtUPHTphhuRsd08dhTTZPobWuSJPVApnx47wK5Zfq5EhTCxzzgSxKWF2T4+Af4SfOuNHEHAF/HkSAAwKMcOnTUBHOcAzv6f2LiYbGVsm+yaWYaV1Pat68tqbXDTQmWydppHi2hkcHiaQKDAmTYswPk5f/OlcP7MmTn38ny5VNL5YpHz3DLIBWAyqfB3gPbDpv1xh1jJKRGkNVDAgBYjIAPAMAt++uk/3vE9NV55fedhQI7e/dmlPp+goMDpE2bWiaw0759HbN06FDHbAsNLfgInLw6WbxBRO0wGf78QHn9xu8k52ierPomXuq3ri39/tvR6qEBqO5yrl6UcwEACPgAACyUn2+TQ3vTjzdM1hmxjjVQPpqWXer7iYgIOhbQOR7Y0XXN4gkM9J2pyhu2q2Oyej4e+4u5/P0LK8zU721Oa2T10ABUsYQVxxs2x/WkYTMAgIAPAKAa5Obkyb87006Y5lzLDzQbpbRiYsIcWTrHgzu1pXHjSEqXjul8dgvZtzVFFr61Vmz5Nvl47CIZ+cGFUrdZtNVDA1ANGT46O2CzLrFWDwcA4AYI+AAAKk32kRw5sC218DTniYfl312pkp9bygY7IhJdv4bpp6PNk0ec1dgR2ImJYeap0hh8WzfZvzVFNizaKUfTc+SDe+bLyPcu9Mj+RABOLmVPmqTsTjfrGuwJOlayCgDwbXwaAICXy8/Ll22r90tq8hGJigmT5t3qmam9KyLzcJYkaYZO4mHZn1Dwv14+VIb+OjqLTO3GkYWnOY+rKXWbR0tI+PFmo7d2i6nQWH2RThN/1cT+8tr138r+eM2kSpWP//eLjHhhUIV/9wDcT/yx2bkU5VwAADsCPgDgxf6ev13mPvOHHE7KdGyLjg2XC+/vI50GNTtp42Qz68uxEiwN6Gjmjl5OP3i01GMIDPY3QRxHUKdFTZO5E9M0SgKDAyr0+FA8naFn+NRB8vJ1c+XI4SzZ/NtumffSKjnv7p5WDw1AJaNhMwDAFQI+AODFwZ6PHlgoUqSS6vCBTLN92JQBJuijGUAHd6c7snTs/ydtOyxZ6Tml/nkhEUGmDEuzdOxBHQ3w1GoYQVaJRTSDatjTZ8mMUT9Kfp5NFr//t9RvXUu6XdDS6qEBqCQanLc3bNZSrsadyIoEABQg4AMAXkiDOJrZUzTYYxzb9unDi+XnNyLl3x2pkpudX+r7jqgT6hTQOV6KFRkTRuNkN9SydwO58L7e8vXTf5jLsyf+JjHNoqRJp7pWDw1AJUjekSqpx7I4m3eNlcAgMicBAAUI+ACAG01RnpuVK9lH8yTniP6fKzm6OK1nH8kr2Kbrha7LK7S/lmI5l3G5kpOVJ/u3Hir2es3MKRrU0f/DokKq4NGjKp16VTvZtyVF/py92QT3Prx3oYz68EKJqksTbMDTJTiXc/WmnAsAcBwBHwDV1ujX04MxR4/mSkZGjqTsST8edHEKuNgvHw/I5JlZq+zXOV9vgjr2oI1jKf305JXFz1/MdN32/joa4KkXV1NimkVLcBgfEd5CM68uerCP6cVk3tcHMuWDexfIrdPPlaAQfs+AJ6NhMwCgOBzlAajURr/WZcYUDqqszM+VzExdckyQxtW6/l9wubjr9XLB+pEjueKNbnj5bGl9akOrh4FqoGUew545S17571w5tC9Ddv2dLHOeWCpXPn4GpXiAh9LPP3v/Hu2j1rBdHauHBABwIwR8AJSr0W9ZmkkWynBxlCG5yno5VppUKEumcNmSqywa/b+oqeLeAgL9JSg0wDTY1Ewa/d+sOy4XXOd8vV6n2wvtX8x1ev/PDZ1tfm8u+/j4FQTxWvbi22BfElE7TK6bOlBev+F7875Z/W28NGhTS/pd18nqoQEoh6T4Q5KRUjBrYlz3+uZvPwAAdgR8ADjoCeDXTy8rsdHv54/+Komr9pmMmuKDMIWDOp4mMNBfatQIkvDwQAkPL/i/4HLB+vasfBeBlqDjARzdFnb8uhMDM4ESEFT1B+WakWWCd5q84fw7PZbMceF9fXy6TM9XNWxbR6587AyZ+eAic/n7aStNf6a2pze2emgAyih+xfH+PZRzAQDcOuDzyiuvyDPPPCP79u2TLl26yEsvvSS9e/c+6e1mzZol11xzjVxyySXy5ZdfVstYAXemWTXZWpZ0+KhkHsqSjMNZkqnLoWP/Oy4fLXS5NFNwZ2XkyO8fbxSr+Af4OQVTig+q9GkSUULQ5sQgjv5v3z/oJDOcTF6dLJ5AM7E0I8tled597lmeh+pxypDmMnBrF1kw/S+x5dtk1rhfZOT7F0rd5tFWDw1AGdCwGQDgEQGfTz75RMaMGSOvv/669OnTR1544QU555xzZNOmTRIbG1vs7bZt2yb33Xef9OvXr1rHC1SXvJx8yUx1DtgUBGmOHM52rJ8YyMmSvNzST7NdWfz8/UzQ5XjJkVPGy7GAjH3dZeZLWIAEhwadeJ1TiVNpp5sd2y2myh+vJ9CgToezmtCAGycY9H9dZd/WFNmwcIccTc+R9++ZLyPfv0DCIpmFDfCUyRUSVu436+E1Q6Req1pWDwkA4GbcJuDz/PPPyy233CI33HCDuayBn2+//VZmzJghY8eOdXmbvLw8GTZsmDz22GOyZMkSOXSo+OmFAW/OuqlokCYsKljCo0NM9kxSwuGT3kZn+2nRrZ4jcOPcN4bmr+5HgztxPfnmF4X5+/vJVRP7yevXf2cCP8nbU2XWuMUyYtogAoKAB9i76aAcTcs263E96pv3NAAAbhfwyc7OlpUrV8q4ceMc2/z9/WXw4MGydOnSYm/3+OOPm+yfm266yQR8TiYrK8ssdmlpaZUwevii3Nx8OXjwiPz771H591/n/4vfdiD5SJVn3WjwRQM3BUuo+cbv+OWQwpdrhpr/QyODHQeJ+m3hlAs+P2mj31OvaMsJIeAFQsKDTBPnV66ba4LPm3/fLT+8uFLOv6eX1UMDUJbp2HsR1AcAuGnAJzk52WTr1KtXr9B2vfzPP/+4vM2vv/4qb7/9tqxZs6bUP2fSpEkmGwhwlXWj03ifLHBz8KCuH5XDh48HDquCJsmERbsK1oS6Dt4cWzTLpiI0iEOjX8C31G4UKcOmnCVvj/xR8nNtsuSD9VK/dS3pfmErq4cGoJQNm1vSsBkA4K4Bn7LSzJzrrrtOpk+fLjExpe/ToRlE2ifIbvfu3dKhQ4cqGqXv0ewQK/uEaPbMkdQiJVKO9WJ63RzOMj1y1JQqGldYWKDUqRMmedoYuBxZN9WNRr+A79GSP31/fz15mbk854nfJaZZtDQ9pa7VQwPggh67bFtV0L8nMiZM6rag4ToAwE0DPhq0CQgIkP37Cz647PRy/fonfmMRHx9vmjVfdNFFjm35+QUn7YGBgabRc8uWLU+4XUhIiFnsUlNTK/mR+K6/5293HSC4v+wBgkK9bkxj4mMBG5eBnON9b7TpaFVn3dSuHSZ16oSaAE7t2qGO9YLF1XqohIUFedTMTopGv4DvOfXKtrJvy0H584vNkpudLx/eu0Du+OgiiaobbvXQABSxa0OyZB/JdZRz0T8PAOC2AZ/g4GDp0aOHzJ8/X4YOHeoI4OjlO+6444T927VrJ+vWrSu07eGHHzaZP9OmTZMmTZpU29hREOwxJUBFer5oH5iP7l8ol0843XxLXJ6sm+rsdXN6y+gTgjXOAZyaNUN9qiEijX4B36InjBc90EcOJB6WxFX7JS35iHwwZoHcOv3cCpeLAqjC6dgp5wIAFMNtjuC01GrEiBHSs2dP6d27t5mWPSMjwzFr1/Dhw6VRo0amD09oaKh06tSp0O1r1qxp/i+6HVVfxqWZPS4b/B7b9sVjv1XZz9cvtEKjXJdI1Sja98apdMrVyQvTeAPwdYFBAXLtMwPklf9+I4f2Zsiu9cky+4nfzWxeZBAA7tmwuSUNmwEA7h7wufrqq+XAgQMyfvx42bdvn3Tt2lV++OEHRyPnHTt2mJm74F605Me5jKs6ZpgKi3Ja1143lBkBQKWJqBUqw6cOkteu/05yjubKmu8SpEHr2tJ/BF+oAO4gJytXtv9V0AahZoMaUqtRhNVDAgC4KbcJ+Cgt33JVwqUWLVpU4m3ffffdKhoVSqL9XUqjWbdYadwhpsxZNwCA6tegTW25auIZ8tH9BZ+9P7y4QmJb1pR2ZzS2emiAz9u57oDps6Va9qR/DwCgeJxho0K0mW9pnH17N/rBAIAH6TSouQy6tYvMf/MvsdlEZv3vFxn53gUS26KghBqA9eVc2rAZAIDiUAuDCtGZm3Q2LinuyyU/keh64WY/AIBnGXhrV+k4oKlZz0rPMU2cj6RmWT0swKcVatjci4bNAIDiEfBBhWj/HJ163Sga9Dl2+cL7+tBnBwA8kM5MeOXEflK/VS1zOXl7qnw87hfJy63amRQBuJZ9JEd2/H3ArNdpGiXR9WpYPSQAgBvjLBwV1mlQMxk2ZYBE1w0vtF0zf3S7Xg8A8Ewh4UEy/IWBUqNmiLm8Zeke+eHFlVYPC/BJ21YnSX5uwTSoZPcAAE6GHj6oFBrU6XBWEzNrlzZy1t4+WsZFZg8AeL5aDSPNdO1v3z7PnGz++uF6qd+6lvS4qJXVQwN8SsIKp3IueiMCAE6Cs3FUGg3uaGPmrufGmf8J9gCA94jrUV8ufuBYCa+IzHnid9mxNsnSMQG+3LC5RU8yfAAAJeOMHAAAlEqfK9pJnyvamvW8nHz58L6Fcjgpw+phAT7haFq27N74r1mv16qmRNYp3UypAADfRcAHAACU2oX395YWPQpmXkxLPmJm7so5mmv1sACvl7hqv9jyC/r3aCY1AAAnQ8AHAACUWmBQgFw7ZYDUahhhLu/e8K/Mnvi72GwFJ6IAqkY807EDAMqIgA8AACiTiFqhct3zAyU4rGDuhzXfJ8ji9/62eliATwR8/PwKemoBvuC1116Tzp07S1RUlFn69u0r33//faluO2vWLPHz85OhQ4dW+TgBd0XABwAAlFmDNrXlysf7OS7Pe2ml/LNkp6VjArxVRspR2bclxaw3aFtHwqJCrB4SUC0aN24skydPlpUrV8qKFStk4MCBcskll8j69etLvN22bdvkvvvuk379jn9OAb6IgA8AACiXToOayaD/62rWtaJr1kOLJSnhkNXDArxOwsrjs3NRzgVfctFFF8n5558vrVu3ljZt2siTTz4pERERsmzZsmJvk5eXJ8OGDZPHHntM4uLiqnW8gLsh4AMAAMpt4C1dTOBHZaXnyPv3zJcjqVlWDwvwKglO07G37E3DZvgmDeRomVZGRoYp7SrO448/LrGxsXLTTTdV6/gAd1RQfA8AAFAO/v5+csVjZ0jyjlRTcvLvzjSZOfYXuf7FwRIQyPdKQGX27/EP8JPmXQtmyQM8WVpamqSmpjouh4SEmMWVdevWmQDP0aNHTXbPnDlzpEOHDi73/fXXX+Xtt9+WNWvWVNnYAU/CkRgAAKiQkPAgGT51oNSoWXCwvnXZHvl+2gqrhwV4hdQDmXJg22Gz3rhjjITUCLJ6SECFacAmOjrasUyaNKnYfdu2bWsCOH/88YfcfvvtMmLECNmwYYPLINJ1110n06dPl5iYmCp+BIBnIMMHAABUWK2GkTLsmQHy1u3zJD/XJr99tEEatK4lPS5ubfXQAI+WsOJ4OVdcT8q54B00YNOoUSPH5eKye1RwcLC0atXKrPfo0UOWL18u06ZNkzfeeKPQfvHx8aZZs/b9scvPzzf/BwYGyqZNm6Rly5ZV8GgA90XABwAAVIoWPerLxQ+cKl8+tdRcnvPkUolpFi3NusRaPTTA48u5FA2b4S0iIyPNNOvloUGcrKwTe8W1a9fOlH85e/jhh03mjwaImjRpUu7xAp6KgA8AAKg0fa5oa3r5LPvsH8nLyZcP71sgd3x4kUTXq2H10ACPDvgEBPkTPIXPGTdunJx33nnStGlTE7iZOXOmLFq0SObNm2euHz58uMkU0pKw0NBQ6dSpU6Hb16xZ0/xfdDvgK+jhAwAAKtWF9/WWuJ4FmQjp/x6VD8YskJyjuVYPC/A4KXvSJGV3ullv2rmuBIXyXS18S1JSkgnqaB+fQYMGmXIuDfYMGTLEXL9jxw7Zu/d4FhyAwvjUAAAAlUozEa59+ix55bq5krInXXZv/Fe+ePw3ufrJ/lYPDfAo8c7Tsfeifw98j864VRLN9inJu+++W8kjAjwLGT4AAKDS1agVKsOnDpLgsILvlv76IVEWv/e31cMCPLh/DwEfAEDZEPABAABVon7rWnLVxH6Oy/NeWilz58ZbOibAU9hsNscMXVrK1bgT00wDAMqGgA8AAKgyHQc2k8G3dzPrNpvItdd+Kxs2JFs9LMDtJe9IldSkTLPevGusBAYFWD0kAICHIeADAACq1MCbO0unwc3MelpatlxyyZdy8OARq4cFuLUE5/49vSnnAgCUHQEfAABQpfz8/OTKx86QBm1qmctbtx6Sq6+eK7m5+VYPDfCI/j32We8AACgLAj4AAKDKBYcFyXXPD5K6dcPM5Z9/3i733/+L1cMC3L5/T0hEkDRsV8fqIQEAPBABHwAAUC1qNYyQL764RAIDCw4/XnhhpbzzzjqrhwW4nf3xhyQj5ahZb9GtngQce88AAFAWfHoAAIBq069fY3n11cGOy7fd9rP8/vtuS8cEuBumYwcAVAYCPgAAoFrdcktnGTWqq1nPzs6Tyy77SnbuTLV6WIDbSHAO+NCwGQBQTgR8AABAtZs6dYAMGNDErO/fnylDh34lmZk5Vg8LsFx+Xr4krNxv1sNrhki9VgXNzgEAKCsCPgAAoNoFBQXIZ59dLC1aRJvLq1btl5tummea1QK+bO+mg3I0Ldusx/WoL/7+flYPCQDgoQj4AAAAS9SpEyZffz1UIiKCzOVZs/6RyZP/tHpYgKXilxfMzqXi6N8DAKgAAj4AAMAynTrVlQ8/vMBx+aGHlsg338RbOibASvErnPr39Kxv6VgAAJ6NgA8AALDUJZe0kokTTzfrWtE1bNi3smFDstXDAqpdXk6+bFtV0L8nMiZM6h4reQQAoDwI+AAAAMs99NCpcuWVbcx6Wlq2XHzxl3Lw4BGrhwVUq10bkiX7SK6jnMvPj/49AIDyI+ADAAAspye277xzrnTtGmsux8cfkquu+kZyc/OtHhpgzXTslHMBACqIgA8AAHALNWoEy1dfDZW6dcPM5fnzd8i99y6yeliAJQ2bW9KwGQBQQQR8AACA22jaNEpmz75EgoIKDlFefHGVvP32OquHBVS5nKxc2b42yazXrF9DajWKsHpIAAAPR8AHAAC4lTPOaCyvvjrYcfn223+S337bbemYgKq2c90Byc3Kc2T30L8HAFBRBHwAAIDbufnmznLnnd3Mek5Ovlx22VeyY0eq1cMCqqWcSxs2AwBQUQR8AACAW3ruubNk4MCmZj0pKVOGDv1SMjNzrB4WUPUNm3vRsBkAUHEEfAAAgFsKCgqQTz+9SOLios3l1auT5MYbfxCbzWb10IBKlX0kR3b8fcCs12kaJdH1alg9JACAFyDgAwAA3FadOmHy9deXSkREkLn8ySebZNKkP6weFlCptq1OkvzcgkAm2T0AgMpCwAcAALi1jh1j5KOPLhB7D9uHHvpVvv56q9XDAipNwgqncq6e9O8BAFQOAj4AAMDtXXxxK3niiTMcl4cN+1bWr0+2dExAVTRsbtGTDB8AQOUg4AMAADzCuHF95Oqr25r19PQcufjiOfLvv0esHhZQIUfTsmX3xn/Ner1WNSWyTpjVQwIAeAkCPgAAwCP4+fnJjBnnSrduseZyQsJhueqqbyQnJ8/qoQHllrhqv9jyC/r3xFHOBQCoRAR8AACAxwgPD5KvvhoqsbHh5vKCBTvk3nsXWT0soNzimY4dAFBFCPgAAACP0qRJlMyefYkEBRUcxrz00mp56621Vg8LqFDDZm1KHteDgA8AoPIQ8AEAAB7n9NMbyWuvDXFcHjnyZ9m2er+lYwLKKiPlqOzdnGLWG7StI2FRIVYPCQDgRQj4AAAAj3TTTafIXXd1N+s5Ofny4X0L5dDedKuHBZRawsrjs3NRzgUAqGwEfAAAgMd67rmzZPDgZo5siffHLJDsIzlWDwsolQSn6djjetGwGQBQuQj4AAAAjxUY6C+ffHKhtGxZ01zeu+mgfP7ob2KzFcx6BHhCw2b/AD9p0a2e1cMBAHgZAj4AAMCj1a4dZmbuCqkRZC6v+2mbLHybJs5wb6kHMuXAtsNmvXHHGMfrFwCAykLABwAAeLyOHWPk6if6m5mO1E+vrpYNi3ZYPSygWAkrnMq5elLOBQCofAR8AACAV2h/ZhM5e1RBE2f1ycOLZd/WghmQAHct51I0bAYAVAUCPgAAwGucecMp0vmcFmY9OzNX3r9nvmQcOmr1sIBiM3wCgvylWZdYq4cDAPBCBHwAAIDX8PPzk8vHny4N29Uxl1N2p8vMBxZJXk6+1UMDHFL2pMnBXWlmvWnnuhIUGmj1kAAAXsitAj6vvPKKNG/eXEJDQ6VPnz7y559/Frvv9OnTpV+/flKrVi2zDB48uMT9AQCAbwgOC5Trnh8oEXVCHZkU3z7PMQLcR7zTdOwtmY4dAODtAZ9PPvlExowZIxMmTJBVq1ZJly5d5JxzzpGkpCSX+y9atEiuueYaWbhwoSxdulSaNGkiZ599tuzevbvaxw4AANxLzfo15L/PDjTlMmrpJ//In19ssnpYgEHDZgCATwV8nn/+ebnlllvkhhtukA4dOsjrr78u4eHhMmPGDJf7f/TRRzJy5Ejp2rWrtGvXTt566y3Jz8+X+fPnV/vYAQCA+9G+KEPH9XVc/urpZZK4ar+lYwJsNpujYXNQaIA0OSXG6iEBALyUWwR8srOzZeXKlaYsy87f399c1uyd0sjMzJScnBypXbt2sftkZWVJamqqY0lLK6idBgAA3qnn0NZy2jXtzXp+rk0+un+hpOxJt3pY8GHJO1IlNSnTrDfvWk8CgwKsHhIAwEu5RcAnOTlZ8vLypF69eoW26+V9+46nvJbkwQcflIYNGxYKGhU1adIkiY6OdiyaSQQAALzb+ff0klZ9CspmMlKOygdj5kv2kRyrhwUfleDUvyeO6dgBAN4e8KmoyZMny6xZs2TOnDmm4XNxxo0bJ4cPH3YsGzZsqNZxAgCA6hcQ6C/XTD5L6jSJNJf3bk6Rzyb8akprgOpmL+dSNGwGAHh9wCcmJkYCAgJk//7CdfV6uX79kr/5ePbZZ03A58cff5TOnTuXuG9ISIhERUU5lsjIggM/AADg3cKjQ2T41EESUiPIXP775+2y4K21Vg8LPkaDjPaGzSERQdKwXR2rhwQA8GJuEfAJDg6WHj16FGq4bG/A3Lfv8WaLRU2ZMkUmTpwoP/zwg/Ts2bOaRgsAADxRbFxNufrJ/uLnV3D559dWy/oF260eFnzI/vhDpqxQtehWz2SfAQBQVdzmU0anZJ8+fbq89957snHjRrn99tslIyPDzNqlhg8fbkqy7J5++ml55JFHzCxezZs3N71+dElPpxEjAABwrX3/JnL2Hd0dlz99ZIns25Ji6ZjgOyjnAgD4ZMDn6quvNuVZ48ePN1Otr1mzxmTu2Bs579ixQ/buPf4h+dprr5nZva644gpp0KCBY9H7AAAAKM6Z158iXc5tYdazj+TK+/fMd2RdAFXJXs6lWvYm4AMAqFqB4kbuuOMOs7iyaNGiQpe3bdtWTaMCAADexM/PTy4ff7okb0+V3Rv/NdO0z3xwkdz4ytkSEOQ234XBy+Tn5TsCPuE1Q6Req1pWDwkA4OU4qgEAAD4nKDRQrnt+oETUKZjdU0/E5z77p9XDghfbu+mgHE3LNutxPeqLv/+xZlIAAFQRAj4AAMAnRderIf99dqAjq2fZZ//IH59vsnpY8FLxTuVccT1LnoUWAIDKQMAHAAD4rGZdYuXSh47PCPr1lGWSuPL4iTlQWWjYDJSd9m3t3LmzREVFmUVncP7++++L3V8nAerXr5/UqlXLLIMHD5Y//yR7E76LgA8AAPBpPS5uLacP62DW83Nt8tH9CyVlT5rVw4IXycvJl22r9pv1yJgwqdsi2uohAR6hcePGMnnyZFm5cqWsWLFCBg4cKJdccomsX7++2L6v11xzjSxcuFCWLl0qTZo0kbPPPlt2795d7WMH3AEBHwAA4PPOG91TWp3a0KxnHMqS9+9ZIFmZOVYPC15i14ZkMyOcvZxLG4cDOLmLLrpIzj//fGndurW0adNGnnzySYmIiJBly5a53P+jjz6SkSNHmlmf27VrJ2+99Zbk5+fL/Pnzq33sgDsg4AMAAHxeQKC/XDv5TKnTJNJc3rclRT6f8Kvk59usHhq8QALlXECF5eXlyaxZsyQjI8OUdpVGZmam5OTkSO3atat8fIA7IuADAAAgImFRITJ86iAJiQgyl/+ev10WvvWX1cOCF4hffrwvFAEfQCQtLU1SU1MdS1ZWVrH7rlu3zmT1hISEyG233SZz5syRDh0KynBP5sEHH5SGDRuaXj6ALyLgAwAAcExsXE35z1Nnir3i5ufX15jAD1BeOVm5sn1tklmvWb+G1GoUYfWQAMtpwCY6OtqxTJo0qdh927ZtK2vWrJE//vhDbr/9dhkxYoRs2LDhpD9De/9oRpAGiEJDQyv5EQCeIdDqAQAAALiTdmc0lnPu7CE/vLjSXP5s/BJT6tWgDSUBKLud6w5IblaeI7uH/j2AmIBNo0aNHJc1e6c4wcHB0qpVK7Peo0cPWb58uUybNk3eeOONYm/z7LPPmoDPzz//bGb5AnwVGT4AAABF9B/RSbqeF2fWtdnu+/fMl/SUo1YPCx5ezhVHORdgREZGOqZa16WkgE9R2oS5pBKwKVOmyMSJE+WHH36Qnj17VtKIAc9EwAcAAKAIzcK47JHTpFGHOubyob0ZMvOBhWZ6baD8DZvrWzoWwNOMGzdOFi9eLNu2bTO9fPSyTr0+bNgwc/3w4cPNNrunn35aHnnkEZkxY4Y0b95c9u3bZ5b09HQLHwVgHQI+AAAALgSFBsp1zw+UyJgwczlx5X755tk/rB4WPEj2kRzZ+XeyWa/TNEqi69WwekiAR0lKSjJBHe3jM2jQIFPONW/ePBkyZIi5fseOHbJ37/Gg6muvvSbZ2dlyxRVXSIMGDRyLlngBvogePgAAAMWIjq0h/312gLx5yw8mu+ePzzZJg9a1pM8V7aweGjzAtjVJkpdbkBXWsifZPUBZvf322yVer9k+zjQTCMBxZPgAAACUoGnnWLn04dMcl7+e8ockrDzelwUoXTkX/XsAANWLgA8AAMBJ9LiolZzx345mPT/XJjPvXygpe9KsHhY8qGFzCzJ8AADVjIAPAABAKZx7Vw9p3behWc84lCXv37NAsjJzrB4W3NTRtGzZvfFfs16vZU2JrFPQCwoAgOpCwAcAAKAUAgL95ZpJZ5rmu2rflhT57JElkp9vs3pocEOJq/aL7dhrg+nYAQBWIOADAABQSmFRITJ86kAJiQgyl9cv3CEL3lxj9bDghuKZjh0AYDECPgAAAGUQ26KmyfTx8yu4PP/Nv+Tv+cwMg8ISVhQEfPR1EteDgA8AoPoR8AEAACijtqc3lnPv6um4/Okjv8rezQctHRPcR0bKUdm7OcWsN2hbx2SGAQBQ3Qj4AAAAlEO/4R2l6/lxZj3naK68f898SU85avWw4AYSVx2fnYtyLgCAVQj4AAAAlIOfn59c9vBp0rhjjLl8aG+Gma49NyfP6qHBYvF/Hg/40LAZAGAVAj4AAADlFBQaKP99boBExoQ5Zmb6ZsofVg8LbtKw2T/AT1p0q2f1cAAAPoqADwAAQAVEx9aQ/z43UAKDCw6r/vxisyz77B+rhwWLpB7IlAPbDpv1Rh1iJKRGwYxuAABUNwI+AAAAFdT0lLpy6cOnOS5/88wfjlma4FsSVjj376GcCwBgHQI+AAAAlaD7ha2k33UdzXp+rk0+emCRHNydZvWwYFE5l6JhMwDASgR8AAAAKsm5d/WQNqc1MuuZh7Lkg3sWSFZmjtXDggUZPgFB/tKsS6zVwwEA+DACPgAAAJXEP8Bf/jOpv8Q0izKX921Nkc8eWSL5+Tarh4ZqkLInTQ7uKsjqatq5rmnqDQCAVQj4AAAAVKKwyBAZPnWQhEYUNOtdv3CHzH9jjdXDQjWIX07/HgCA+yDgAwAAUMnqNo+W/0w6U/z8/czlBdP/knU/bbN6WKhC+Xn58te8RMfl5t3p3wMAsBYBHwAAgCrQ9vTGct7oHo7Ln034VfZs+tfSMaFq/D1/uzx9weeyddkex7ZPH15stgMAYBUCPgAAAFXkjP92lG4XtDTrOUdzTRPn9INHrB4WKpEGdT56YKGkJmUW2p56INNsJ+gDALAKneQAAACqiJ+fn1z6cF85sP2w7Po7WQ7ty5CP7l8kN71+tgQGBVg9PDix2WySczRPso/mSnZmjmRn5poZ1rKP5Er2kYLL+n+W/n9su16/+tt4EVc9uXWbn8jcZ/+QDmc1MQ29AQCoTgR8AAAAqlBQSKBc99xAeXnYN5KWfES2rd4vX0/+wwSCNCCEssvNySsIwNgDL0ecgjRHciTniFOwJrMgSGO22QM3us0Eco7fh/5vq+zJ1Gwih/dnmt95XE+aOAMAqhcBHwAAgCoWVTdcrnt+oLx58/eSm50vy+dslvqtakr91rUkNfmIRMWESfNu9bwuCyQvL18yMnIkPV2XbPN/weVsF9sKb/9rT4Yji8aeXVMQmMmVvNx88ST6OwYAoLoR8AEAAKgGTTrVlcseOV0+fWSJufzNM38Wuj46NlwuvL+PdBrUzLpypiNFS5mOZ8g4lzXp9m3hgScN4hw5kivuKiDIX4LDAiU4PEhCjv2vl0PCgyTI/B8owWFBEhx+bFvosW1O+yUlHpI5Tyw96c/SgB4AANWNgA8AAEA10QbOf/+8TTb8svOE6w4fa/I7bMqAYoM+GpjJy8k3AZkcF6VM9gwYR8lSkR40RQM59gwava+yljMVhK2qnk5tb4IuYa4DMcGhGoQ5MXBjtoUFHQ/SmP0KLuv9VEYPpaad68qCN/8yvzuXfXz8CgJ5mr0FAEB1I+ADAABQTfLz8mXXxmKmZrcdn857+Zf1zaxezhk19iyb/NzKbjRTecLDAyUiIlhq1AiSiAhdggv972r7idsK9ns7Md0EcAJDAty215GW4GlWlgbqNLhTKOhzbMgX3tfH60r1AACegYAPAABANdHmvUWn7y4qJytPNv+2u+rLmYpmxBwrU7JnxtizZMw2F/vd1r2uUxAn2AR7AioxsBFxyH3LwZxpNpZmZc195g857PS7NSV691lTogcAgCLgAwAA4KbNe53LmU4WiHEEb4qWPzn1nNH/K6ucqWvXmArfh7fQoI5OvW4Cel7chBsA4FkI+AAAAFST0jbv/e9zA6RN30ZuXc6EwjS4w9TrAAB3wtcOAAAA1USzPrTUx97fxWWT33rh0r5/EzMrFMEeAABQXgR8AAAAqrnJr1E0lkOTXwAAUIk4mgAAALCgyW903fBC2zXzp6Qp2QEAAMqCHj4AAADVjCa/AACgqhHwAQAAsABNfgEAQFXiayQAAAAAAAAvQ8AHAAAAAADAyxDwAQAAAAAA8DIEfAAAAAAAALwMAR8AAAAAAAAvQ8AHAAAAAADAyxDwAQAAAAAA8DIEfAAAAAAAALwMAR8AAAAAAAAvQ8AHAAAAAADAyxDwAQAAAAAA8DJuFfB55ZVXpHnz5hIaGip9+vSRP//8s8T9P/vsM2nXrp3Z/5RTTpHvvvuu2sYKAAAAAADgrtwm4PPJJ5/ImDFjZMKECbJq1Srp0qWLnHPOOZKUlORy/99//12uueYauemmm2T16tUydOhQs/z999/VPnYAAAAAAAB34jYBn+eff15uueUWueGGG6RDhw7y+uuvS3h4uMyYMcPl/tOmTZNzzz1X7r//fmnfvr1MnDhRunfvLi+//HK1jx0AAAAAAMCduEXAJzs7W1auXCmDBw92bPP39zeXly5d6vI2ut15f6UZQcXtDwAAAAAA4CsCxQ0kJydLXl6e1KtXr9B2vfzPP/+4vM2+fftc7q/bi5OVlWUWu8OHD5v/9+7dK+7o8P6DVg/Bp+zadbRK75/fp/f8PvldVi/em96F96b34L3pXXhveo+qfm9WhP28Kz8/3+qhAD7BLQI+1WXSpEny2GOPnbC9d+/elowH7mWy1QNApeL36T34XXoXfp/eg9+ld+H36T084Xe5f/9+adq0qdXDALyeWwR8YmJiJCAgwLzxnenl+vXru7yNbi/L/mrcuHGmMbRdbm6ubNy4UZo0aWJKyFBxaWlppgfThg0bJDIy0urhoIL4fXoPfpfehd+n9+B36V34fXoPfpdVQzN79JytW7duVg8F8AluEfAJDg6WHj16yPz/b+9OgG2s3wCOP3S51mtNdAmVfV+yc1OWirKnJNfehCxNiGRpKnuuSjVkqxhLSlEjOwmFLAkZhBlLGpIlLvH+53nmf87ccxeunMV5z/czczrOe97zvr/3Pp27POf5Pb9Vq2ylLc83A33cp0+fVF9Tu3Zte75///7ebStWrLDtaYmOjrZbUnXr1vXbdUDk3Llzdh8bGysxMTGhHg5uE/F0D2LpLsTTPYiluxBP9yCWgUNlDxBhCR+llTfx8fFSvXp1m2KVkJAgFy9etFW7VKdOnewbrk7LUv369ZO4uDiZOHGiNGvWTObNmydbt26VqVOnhvhKAAAAAAAAQuuOSfi0b99e/vzzTxk+fLg1Xq5cubIsW7bM25j56NGjPtOu6tSpI3PnzpVhw4bJ0KFDpUSJErJ48WIpX758CK8CAAAAAAAg9O6YhI/S6VtpTeFau3Ztim3t2rWzG+4cOmVuxIgRKabOITwRT/cglu5CPN2DWLoL8XQPYgnADTI4juOEehAAAAAAAADwH5amAgAAAAAAcBkSPgAAAAAAAC5DwgcAAAAAAMBlSPgghdGjR8tDDz0kOXPmlAIFCkjLli3lt99+89nn8uXL0rt3b8mXL5/kyJFD2rRpI3/88YfPPn379pVq1apZsztddS01u3btkvr160uWLFmkSJEiMm7cuIBeW6QJViz1GJ07d5YKFSpIVFSUnQfhG09tkt+iRQspVKiQZM+e3faZM2dOwK8vkgQrlnrMhg0b2oqX+n32/vvvt9Utr169GvBrjCTB/LnpceDAATtf7ty5A3JNkSpYsTx8+LBkyJAhxW3z5s0Bv8ZIEsz3prZFnTBhgpQsWdL2i42Nlbfeeiug1wcAN0PCBymsW7fOfvDpLx0rVqywPwyaNGkiFy9e9O4zYMAAWbJkiSxcuND2P378uLRu3TrFsbp27Srt27dP9Tznzp2z4xYtWlS2bdsm48ePl5EjR8rUqVMDen2RJFixvHbtmmTNmtV+IWrUqFFArymSBSueGzdulIoVK8qiRYssKdulSxfp1KmTLF26NKDXF0mCFctMmTJZ7JYvX25/5CQkJMi0adNs5RmEXzw99PjPPvusfWCC8I7lypUr5cSJE96bJhUQnvHs16+ffPzxx5b02bdvn3z99ddSo0aNgF0bAKSLrtIF3MipU6d0JTdn3bp19vjs2bNOpkyZnIULF3r32bt3r+2zadOmFK8fMWKEU6lSpRTbP/jgAydPnjxOYmKid9vgwYOdUqVKBexaIl2gYplUfHy806JFiwCMHqGIp8cTTzzhdOnSxY+jR6hiOWDAAKdevXp+HD2CHc9BgwY5HTt2dGbOnOnkypUrQFeBQMby999/t9ds3749wFeAYMRzz549TlRUlLNv374AXwEA3BoqfHBTf//9t93nzZvX7rUaRz8hSVrJUbp0abnvvvtk06ZN6T6u7tugQQPJnDmzd1vTpk3tU+i//vrLr9eAwMYS7o+nnstzHoRvLHUa0LJlyyQuLs4Po0Yo4rl69WqrRJgyZYqfR41QvDefeuopm2pUr149qwhBeMZTK4R0yqxWwhYvXlyKFSsm3bt3lzNnzgTgKgAg/Uj44IauX78u/fv3l7p160r58uVt28mTJy1Jk7xvgPaI0OfSS/fV1yQ/huc5hE8s4e54LliwQLZs2WJTuxCesaxTp4718ClRooRNA3rjjTf8Nn4EL56nT5+2fmmzZs2SmJgYv48dwYul9oqZOHGiJe+++eYbS/hofxmSPuEZz0OHDsmRI0csnp988om9RzWZ1LZtW79fBwDciqhb2hsRR+c97969WzZs2BDqoeA2EUt3CVY816xZY4ke7ftSrly5gJ4rUgUjlvPnz5fz58/Lzp07ZeDAgdZjYtCgQQE7XyQLZDx79OghHTp0sOpYhHcs8+fPLy+//LL3sTYW1t4x2s9Qq34QXvHUZFJiYqIle7Rps5o+fbr1ZNLK9VKlSvn9nACQHlT4IE19+vSx0lT9g69w4cLe7QULFpQrV67I2bNnffbXFQ30ufTSfZOvguB5fCvHQehjCXfGU5tXPvnkkzJp0iRr/IvwjaWugli2bFlr9DtmzBhrkK/N1hFe8dTpXJqs09UQ9datWzeboqL/njFjhl+vJdKF4udmzZo1bdolwi+euqqlvg89yR5VpkwZuz969KhfrgEA/gsSPkh1WUn9wfjll1/aL5c6Fzkp/bRCV35ZtWqVd5t+eqE/0GrXrp3u8+i+69ev91keWFdQ0E9B8uTJ46eriWzBiiXcF09dmr1Zs2YyduxY6dmzp9+uAaF/b+on0fp9V+8RXvHUniI7duzw3nRqni43rf9u1aqVX68pUoXyvalx1MQBwi+eOk3s33//lYMHD3q37d+/3+51NVoACBWmdCHVkte5c+fKV199Zb9IeuYw58qVy5be1nv9VFFLkbXpnfYReOmll+wHY61atbzH0U+pLly4YK+/dOmS/SKj9FNmnS+tZemjRo2yYw0ePNjKbCdPnmzVBAivWKo9e/bYp2TaoFCnjnj2qVy5ckiu3Y2CFU/9BLR58+a2xGybNm2859HnaNwcXrGcM2eO/TFToUIFiY6Olq1bt8qQIUNsaWHdjvCKp6diwEPjmTFjRm8/EoRPLGfPnm33VapUse1ffPGFVWnpst4Iv3hq0+eqVava0u0JCQmWUNdzN27c2KfqBwCC7hZX9UIE0P8tUrvp8q8ely5dcnr16mXLqmfLls1p1aqVc+LECZ/jxMXFpXocXYrUY+fOnbY8cHR0tBMbG+uMGTMmqNfqdsGMZdGiRVPdB+EXz/j4+FSf19chvGI5b948p2rVqk6OHDmc7NmzO2XLlnXefvttOzbC83ttUizLHr6xnDVrllOmTBl7fUxMjFOjRg2fpcERfu/NY8eOOa1bt7bvt/fcc4/TuXNn5/Tp00G9XgBILoP+J/hpJgAAAAAAAAQKPXwAAAAAAABchoQPAAAAAACAy5DwAQAAAAAAcBkSPgAAAAAAAC5DwgcAAAAAAMBlSPgAAAAAAAC4DAkfAAAAAAAAlyHhAwAAAAAA4DIkfAAA8KO1a9dKhgwZ5OzZs3KnOHz4sI1px44dfj1usWLFJCEhwa/HBAAAgH+Q8AEA4P86d+5siRG9ZcqUSYoXLy6DBg2Sy5cvh3pod6QtW7ZIz549Qz0MAAAApCIqtY0AAESqxx57TGbOnClXr16Vbdu2SXx8vCWAxo4dG+qh3XHuvvvuUA8BAAAAaaDCBwCAJKKjo6VgwYJSpEgRadmypTRq1EhWrFjhfT4xMVH69u0rBQoUkCxZski9evWs0iUt//zzjzz++ONSt27dVKd5LV26VHLnzi3Xrl2zxzrtShNMr776qnef7t27S8eOHeXixYsSExMjn3/+uc8xFi9eLNmzZ5fz58/b459++kmqVKli46tevbps377dZ389V7du3ayCKWvWrFKqVCmZPHlyimonvf4JEyZIoUKFJF++fNK7d29LhKU1peudd96RChUq2Fj069erVy+5cOFCur7uAAAA8C8SPgAApGH37t2yceNGyZw5s3ebTvFatGiRzJ49W37++Wd58MEHpWnTpnLmzJkUr9cET+PGjeX69euWNNLETnL169e3RI0nKbNu3TrJnz+/9QLy0G0PP/ywJVKeeeYZq0BKSh+3bdtWcubMaQmW5s2bS9myZa1CaeTIkfLKK6/47K/jKVy4sCxcuFD27Nkjw4cPl6FDh8qCBQt89luzZo0cPHjQ7vV6Z82aZbe0ZMyYUd5991359ddfbf/Vq1fb1wsAAADBR8IHAIBkFTc5cuSw6hitVjl16pQMHDjQntMKmw8//FDGjx9vVTuaVJk2bZpVyUyfPt3nOCdPnpS4uDirjlmyZIlky5Yt1fPlypVLKleu7E3w6P2AAQMsAaTJm2PHjsmBAwfsWJ5qn++++05OnDhhj3V83377rXTt2tUez5071xI6Op5y5cpZ8sczfg/tTzRq1Cir/tEqn+eee066dOmSIuGTJ08eef/996V06dJ2nGbNmsmqVavS/Nr1799fGjZsaJU/jzzyiLz55pspjgkAAIDgIOEDAEASmrDQaVU//vij9e/RREibNm3sOa120SlNOj0rafKkRo0asnfvXp/jaGWPVv/Mnz/fp0IoNZrM0USP4zjy/fffS+vWraVMmTKyYcMGq+659957pUSJEravnksTOVpBoz777DMpWrSoNGjQwB7rOCpWrGgJK4/atWunOOeUKVOkWrVq1odHE1xTp06Vo0eP+uyj57nrrru8jzV5pQmmtKxcuVIeffRRiY2NtWqj559/Xk6fPm3T2gAAABBcJHwAAEhCp01poqZSpUoyY8YMS/wkr95JD62GWb9+vU2ZuhmdrqXJnZ07d1oCSStqdJsmgTTh46nu8dAqH8/UKp3OpUkp7fuTXvPmzbNpXtrHZ/ny5Zbg0mNcuXLFZz8dS1J6Dq0eSmvpd60C0mSTTnnT6WSaVFLJjwsAAIDAI+EDAMANetJob5thw4bJpUuX5IEHHrBqnR9++MG7j1b8aNNmnd6V1JgxY6xCSCtebpb08fTxmTRpkje540n46E3/nZQ2cD5y5Ij1y9Fj63k8tDJo165dPkvJb9682ef1Ov46depYU2Vt7qwJLq1euh2a4NFk0MSJE6VWrVpSsmRJOX78+G0dEwAAAP8dCR8AAG6gXbt2Nq1Jq1W0+ufFF1+0njjLli2zZEuPHj1sypJWyySnK1xpfxztZ7Nv3740z6G9crQyZs6cOd7kjk7R0qbQ+/fvT1Hho/vrtC8dR5MmTawBs0eHDh2sEkfHpePT/j46jqR0etjWrVutF5Ae//XXX7/hSmPpoUkjTX699957cujQIfn000/lo48+uq1jAgAA4L8j4QMAwA1ERUVJnz59ZNy4cda0WSt3tKeP9qepWrWqNVTWxIkmYVKjVTtPP/20JX00uZIWTerocumehE/evHmtakiXiNdl05PTBJNOlfI0a/bQfjzaJPqXX36x6p3XXntNxo4d67PPCy+8YAmj9u3bS82aNa3Pjlb73A6dAqfLsuu5ypcvb8mr0aNH39YxAQAA8N9lcLRDJAAACCtaQaOreem0qZs1hQYAAEDkiQr1AAAAQPrp9DFdkl0rjbRSh2QPAAAAUsOULgAAwohOLdNVvHSq15AhQ0I9HAAAANyhmNIFAAAAAADgMlT4AAAAAAAAuAwJHwAAAAAAAJch4QMAAAAAAOAyJHwAAAAAAABchoQPAAAAAACAy5DwAQAAAAAAcBkSPgAAAAAAAC5DwgcAAAAAAMBlSPgAAAAAAACIu/wPq0TR7M4DHOYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Filtrowanie lat 2010–2016 (włącznie)\n",
    "filtered = movies[(movies[\"release_year\"] >= 2010) & (movies[\"release_year\"] <= 2016)]\n",
    "\n",
    "# Grupowanie i obliczanie średniego budżetu i przychodu\n",
    "grouped = filtered.groupby(\"release_year\")[[\"revenue\", \"budget\"]].mean().reset_index()\n",
    "\n",
    "# Tworzenie wykresu\n",
    "fig, ax1 = plt.subplots(figsize=(10, 6))\n",
    "\n",
    "# Wykres kolumnowy: revenue\n",
    "ax1.bar(grouped[\"release_year\"], grouped[\"revenue\"], color=\"skyblue\", label=\"Średni przychód\")\n",
    "ax1.set_ylabel(\"Średni przychód (USD)\")\n",
    "ax1.set_xlabel(\"Rok wydania\")\n",
    "ax1.set_xticks(grouped[\"release_year\"])\n",
    "ax1.tick_params(axis='y')\n",
    "ax1.set_title(\"Średni przychód i budżet filmów (2010–2016)\")\n",
    "\n",
    "# Wykres liniowy: budget (na tej samej osi)\n",
    "ax2 = ax1.twinx()\n",
    "ax2.plot(grouped[\"release_year\"], grouped[\"budget\"], color=\"darkblue\", linewidth=2, marker=\"o\", label=\"Średni budżet\")\n",
    "ax2.set_ylabel(\"Średni budżet (USD)\")\n",
    "ax2.tick_params(axis='y')\n",
    "\n",
    "# Legenda poza wykresem\n",
    "fig.legend(loc=\"upper right\", bbox_to_anchor=(1.15, 1.0))\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bd000c3c",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'id'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[32m~\\AppData\\Local\\Temp\\ipykernel_18228\\2324927422.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      5\u001b[39m movies[\u001b[33m\"release_date\"\u001b[39m] = pd.to_datetime(movies[\u001b[33m\"release_date\"\u001b[39m], errors=\u001b[33m\"coerce\"\u001b[39m)\n\u001b[32m      6\u001b[39m movies[\u001b[33m\"release_year\"\u001b[39m] = movies[\u001b[33m\"release_date\"\u001b[39m].dt.year\n\u001b[32m      7\u001b[39m \n\u001b[32m      8\u001b[39m \u001b[38;5;66;03m# Łączenie filmów z nazwami gatunków\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m9\u001b[39m merged = movies.merge(genres, left_on=\u001b[33m\"genre_id\"\u001b[39m, right_on=\u001b[33m\"id\"\u001b[39m, how=\u001b[33m\"left\"\u001b[39m)\n\u001b[32m     10\u001b[39m \n\u001b[32m     11\u001b[39m merged[[\u001b[33m\"title\"\u001b[39m, \u001b[33m\"genre_id\"\u001b[39m, \u001b[33m\"name\"\u001b[39m]].head()\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\frame.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[39m\n\u001b[32m  10828\u001b[39m         validate: MergeValidate | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[32m  10829\u001b[39m     ) -> DataFrame:\n\u001b[32m  10830\u001b[39m         \u001b[38;5;28;01mfrom\u001b[39;00m pandas.core.reshape.merge \u001b[38;5;28;01mimport\u001b[39;00m merge\n\u001b[32m  10831\u001b[39m \n\u001b[32m> \u001b[39m\u001b[32m10832\u001b[39m         return merge(\n\u001b[32m  10833\u001b[39m             self,\n\u001b[32m  10834\u001b[39m             right,\n\u001b[32m  10835\u001b[39m             how=how,\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[39m\n\u001b[32m    166\u001b[39m             validate=validate,\n\u001b[32m    167\u001b[39m             copy=copy,\n\u001b[32m    168\u001b[39m         )\n\u001b[32m    169\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m170\u001b[39m         op = _MergeOperation(\n\u001b[32m    171\u001b[39m             left_df,\n\u001b[32m    172\u001b[39m             right_df,\n\u001b[32m    173\u001b[39m             how=how,\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, indicator, validate)\u001b[39m\n\u001b[32m    790\u001b[39m             self.right_join_keys,\n\u001b[32m    791\u001b[39m             self.join_names,\n\u001b[32m    792\u001b[39m             left_drop,\n\u001b[32m    793\u001b[39m             right_drop,\n\u001b[32m--> \u001b[39m\u001b[32m794\u001b[39m         ) = self._get_merge_keys()\n\u001b[32m    795\u001b[39m \n\u001b[32m    796\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m left_drop:\n\u001b[32m    797\u001b[39m             self.left = self.left._drop_labels_or_levels(left_drop)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m   1293\u001b[39m                         \u001b[38;5;66;03m# Then we're either Hashable or a wrong-length arraylike,\u001b[39;00m\n\u001b[32m   1294\u001b[39m                         \u001b[38;5;66;03m#  the latter of which will raise\u001b[39;00m\n\u001b[32m   1295\u001b[39m                         rk = cast(Hashable, rk)\n\u001b[32m   1296\u001b[39m                         \u001b[38;5;28;01mif\u001b[39;00m rk \u001b[38;5;28;01mis\u001b[39;00m \u001b[38;5;28;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1297\u001b[39m                             right_keys.append(right._get_label_or_level_values(rk))\n\u001b[32m   1298\u001b[39m                         \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   1299\u001b[39m                             \u001b[38;5;66;03m# work-around for merge_asof(right_index=True)\u001b[39;00m\n\u001b[32m   1300\u001b[39m                             right_keys.append(right.index._values)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\generic.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, key, axis)\u001b[39m\n\u001b[32m   1907\u001b[39m             values = self.xs(key, axis=other_axes[\u001b[32m0\u001b[39m])._values\n\u001b[32m   1908\u001b[39m         \u001b[38;5;28;01melif\u001b[39;00m self._is_level_reference(key, axis=axis):\n\u001b[32m   1909\u001b[39m             values = self.axes[axis].get_level_values(key)._values\n\u001b[32m   1910\u001b[39m         \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1911\u001b[39m             \u001b[38;5;28;01mraise\u001b[39;00m KeyError(key)\n\u001b[32m   1912\u001b[39m \n\u001b[32m   1913\u001b[39m         \u001b[38;5;66;03m# Check for duplicates\u001b[39;00m\n\u001b[32m   1914\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m values.ndim > \u001b[32m1\u001b[39m:\n",
      "\u001b[31mKeyError\u001b[39m: 'id'"
     ]
    }
   ],
   "source": [
    "\n",
    "movies = pd.read_csv(\"C:/Users/abero/Downloads/tmdb_movies.csv\")\n",
    "genres = pd.read_csv(\"C:/Users/abero/Downloads/tmdb_genres.csv\")\n",
    "\n",
    "\n",
    "movies[\"release_date\"] = pd.to_datetime(movies[\"release_date\"], errors=\"coerce\")\n",
    "movies[\"release_year\"] = movies[\"release_date\"].dt.year\n",
    "\n",
    "# Łączenie filmów z nazwami gatunków\n",
    "merged = movies.merge(genres, left_on=\"genre_id\", right_on=\"id\", how=\"left\")\n",
    "\n",
    "merged[[\"title\", \"genre_id\", \"name\"]].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7fa7638d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>28.0</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12.0</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14.0</td>\n",
       "      <td>Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16.0</td>\n",
       "      <td>Animation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>878.0</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0           genres\n",
       "0        28.0           Action\n",
       "1        12.0        Adventure\n",
       "2        14.0          Fantasy\n",
       "3        16.0        Animation\n",
       "4       878.0  Science Fiction"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "genres.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9e70334",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'genre_id'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[32m~\\AppData\\Local\\Temp\\ipykernel_18228\\1561272580.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m merged = movies.merge(genres, left_on=\u001b[33m\"genre_id\"\u001b[39m, right_on=\u001b[33m\"genre_id\"\u001b[39m, how=\u001b[33m\"left\"\u001b[39m)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\frame.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[39m\n\u001b[32m  10828\u001b[39m         validate: MergeValidate | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[32m  10829\u001b[39m     ) -> DataFrame:\n\u001b[32m  10830\u001b[39m         \u001b[38;5;28;01mfrom\u001b[39;00m pandas.core.reshape.merge \u001b[38;5;28;01mimport\u001b[39;00m merge\n\u001b[32m  10831\u001b[39m \n\u001b[32m> \u001b[39m\u001b[32m10832\u001b[39m         return merge(\n\u001b[32m  10833\u001b[39m             self,\n\u001b[32m  10834\u001b[39m             right,\n\u001b[32m  10835\u001b[39m             how=how,\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[39m\n\u001b[32m    166\u001b[39m             validate=validate,\n\u001b[32m    167\u001b[39m             copy=copy,\n\u001b[32m    168\u001b[39m         )\n\u001b[32m    169\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m170\u001b[39m         op = _MergeOperation(\n\u001b[32m    171\u001b[39m             left_df,\n\u001b[32m    172\u001b[39m             right_df,\n\u001b[32m    173\u001b[39m             how=how,\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, indicator, validate)\u001b[39m\n\u001b[32m    790\u001b[39m             self.right_join_keys,\n\u001b[32m    791\u001b[39m             self.join_names,\n\u001b[32m    792\u001b[39m             left_drop,\n\u001b[32m    793\u001b[39m             right_drop,\n\u001b[32m--> \u001b[39m\u001b[32m794\u001b[39m         ) = self._get_merge_keys()\n\u001b[32m    795\u001b[39m \n\u001b[32m    796\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m left_drop:\n\u001b[32m    797\u001b[39m             self.left = self.left._drop_labels_or_levels(left_drop)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m   1293\u001b[39m                         \u001b[38;5;66;03m# Then we're either Hashable or a wrong-length arraylike,\u001b[39;00m\n\u001b[32m   1294\u001b[39m                         \u001b[38;5;66;03m#  the latter of which will raise\u001b[39;00m\n\u001b[32m   1295\u001b[39m                         rk = cast(Hashable, rk)\n\u001b[32m   1296\u001b[39m                         \u001b[38;5;28;01mif\u001b[39;00m rk \u001b[38;5;28;01mis\u001b[39;00m \u001b[38;5;28;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1297\u001b[39m                             right_keys.append(right._get_label_or_level_values(rk))\n\u001b[32m   1298\u001b[39m                         \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   1299\u001b[39m                             \u001b[38;5;66;03m# work-around for merge_asof(right_index=True)\u001b[39;00m\n\u001b[32m   1300\u001b[39m                             right_keys.append(right.index._values)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\generic.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, key, axis)\u001b[39m\n\u001b[32m   1907\u001b[39m             values = self.xs(key, axis=other_axes[\u001b[32m0\u001b[39m])._values\n\u001b[32m   1908\u001b[39m         \u001b[38;5;28;01melif\u001b[39;00m self._is_level_reference(key, axis=axis):\n\u001b[32m   1909\u001b[39m             values = self.axes[axis].get_level_values(key)._values\n\u001b[32m   1910\u001b[39m         \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1911\u001b[39m             \u001b[38;5;28;01mraise\u001b[39;00m KeyError(key)\n\u001b[32m   1912\u001b[39m \n\u001b[32m   1913\u001b[39m         \u001b[38;5;66;03m# Check for duplicates\u001b[39;00m\n\u001b[32m   1914\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m values.ndim > \u001b[32m1\u001b[39m:\n",
      "\u001b[31mKeyError\u001b[39m: 'genre_id'"
     ]
    }
   ],
   "source": [
    "merged = movies.merge(genres, left_on=\"genre_id\", right_on=\"genre_id\", how=\"left\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4f8f2bf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Unnamed: 0', 'genres'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(genres.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7470dee3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Unnamed: 0', 'budget', 'homepage', 'id', 'original_language',\n",
      "       'original_title', 'overview', 'popularity', 'release_date', 'revenue',\n",
      "       'runtime', 'status', 'tagline', 'title', 'vote_average', 'vote_count',\n",
      "       'genre_id', 'release_year'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(movies.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d5ba4c18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                      title  genre_id genre_name\n",
      "0                                    Avatar      28.0     Action\n",
      "1  Pirates of the Caribbean: At World's End      12.0  Adventure\n",
      "2                                   Spectre      28.0     Action\n",
      "3                     The Dark Knight Rises      28.0     Action\n",
      "4                               John Carter      28.0     Action\n"
     ]
    }
   ],
   "source": [
    "genres = genres.rename(columns={\"Unnamed: 0\": \"genre_id\", \"genres\": \"genre_name\"})\n",
    "\n",
    "merged = movies.merge(genres, on=\"genre_id\", how=\"left\")\n",
    "\n",
    "print(merged[[\"title\", \"genre_id\", \"genre_name\"]].head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "762527e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1881</th>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>8.5</td>\n",
       "      <td>8205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3337</th>\n",
       "      <td>The Godfather</td>\n",
       "      <td>8.4</td>\n",
       "      <td>5893</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>662</th>\n",
       "      <td>Fight Club</td>\n",
       "      <td>8.3</td>\n",
       "      <td>9413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2731</th>\n",
       "      <td>The Godfather: Part II</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3338</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3232</th>\n",
       "      <td>Pulp Fiction</td>\n",
       "      <td>8.3</td>\n",
       "      <td>8428</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2294</th>\n",
       "      <td>Spirited Away</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3840</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1818</th>\n",
       "      <td>Schindler's List</td>\n",
       "      <td>8.3</td>\n",
       "      <td>4329</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3865</th>\n",
       "      <td>Whiplash</td>\n",
       "      <td>8.3</td>\n",
       "      <td>4254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1663</th>\n",
       "      <td>Once Upon a Time in America</td>\n",
       "      <td>8.2</td>\n",
       "      <td>1069</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1847</th>\n",
       "      <td>GoodFellas</td>\n",
       "      <td>8.2</td>\n",
       "      <td>3128</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            title  vote_average  vote_count\n",
       "1881     The Shawshank Redemption           8.5        8205\n",
       "3337                The Godfather           8.4        5893\n",
       "662                    Fight Club           8.3        9413\n",
       "2731       The Godfather: Part II           8.3        3338\n",
       "3232                 Pulp Fiction           8.3        8428\n",
       "2294                Spirited Away           8.3        3840\n",
       "1818             Schindler's List           8.3        4329\n",
       "3865                     Whiplash           8.3        4254\n",
       "1663  Once Upon a Time in America           8.2        1069\n",
       "1847                   GoodFellas           8.2        3128"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Obliczenie 3. kwartylu vote_count\n",
    "q3_vote_count = movies['vote_count'].quantile(0.75)\n",
    "\n",
    "# Filtracja filmów z vote_count > 3 kwartyl\n",
    "filtered_movies = movies[movies['vote_count'] > q3_vote_count]\n",
    "\n",
    "# Sortowanie malejąco po vote_average i wybranie top 10\n",
    "top_10_movies = filtered_movies.sort_values(by='vote_average', ascending=False).head(10)\n",
    "\n",
    "top_10_movies[['title', 'vote_average', 'vote_count']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "01624bde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ekoHNu/D9IQapo3tx5r35nMzn4VJzy4tLbXOP7NuznmTph0dBvKlL33JOsdM7/19993X5Rimh9mM5zfjq817MuO5//e//7U+bq5RmHPD9D63P7/M79+cn+179E0vrdvt3uE4bdPrav4NmD9/foft5jXMvwGdnXrqqa098VH//e9/FQgErF7wKPPZXX755db3a3qHo8y/L+b83plXX31VVVVVHY5pfOtb35LP5+vwmXTHZImYFPDetL8vr2W+F3Pu7oz5HszwEJM9YM69pqambv+djIp+/uazBIDhzm13AwBgoJk/3s0ftStWrLACsJ155ZVXrKJJJvg2f1ibQKOiosL64z4alJuA49lnn9Ull1yimpoaa8yhYVJ9TcBoggqTJllQUGAVnTLH7I4Jhk1QdNppp1lpuqagmElB3XPPPa0Uz/4w7TMBRrSyt0nZLCkpaS1aFmUeMymdJkA3afcmcDTFijoHFybgMIGluYBggiTzR7mpFv3b3/7WCmKizPhUE/Cce+651n0TyJjUUfPHu7lYsffee1vBthmXaQIN89lG3XrrrVa6/9VXX22lnJoLD+Y4Jmhsf1HBpMPut99+VmBvvhOT4myCyOXLl7deVDEpzqeffrqmT59u7WeCBfM8E9APtNdff936LMx3bS4q/OlPf7K+TzMutzfnWmcmffff//63lXZsAiJz3hx//PEd9jHnnjmn2jNjiE3w3D4l2DzXnEPmQoAJlM3na4IcE9S+8cYbViqxOe8+//xz67szVcCj34l5je6YFOR7773XuohhzitzPpixyX1h2mradcghh1jfszm3zDlrAm2Tgm2+d9Ouv/zlL9YFGpPGbIIyw3zn5nMxqdHmMzcXlv75z39aFyfMb8ecm+YcnzdvXoeLHx9++KF1XpnPwJwv0c/UfA4mPT06Trs77733nhUQmvO3N8rLy63b9ue3OT/N++ucbm2+g+jjBx10UJ8+R/Mcw1w0a8983+Z9msfNRam+6qn9A/1aZtpGc0Fjt912s8Zwmwtl5uKI+b7NRZi99tqrw/7mwpGpI2C+P3NhCgCGNbu72gFgoL3wwgthl8tlLXPnzg3/8Ic/DD///PPhpqamLvuafwadTmf4448/7rD9kksuCY8ZMya8ZcuWDtu/8pWvhLOyslrTQX//+99bx3jooYda9/H5fOHddtutS3r5oYceam27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T75c+vwO6b0rpCnfkWpXSStvkaZ8V3aJmZ7uSVnJOqQgTVOzu7nCsQPPr6/T9ByPCtJi42QFAAAA0Hsm9fmNN97QL37xCx1++OEqLi620ptNuvFJJ53UIZ35z3/+s7UtLS1NN998s7X9v//9r/bee2+lpKRYAfuNN96o5ubm1uetWrVKhxxyiPW4GUf84osvdnj9devWWcd+7LHHrNc3c0zPmjVLi994SWqskgK1+sc99+wwvTx6jAceeEAHHnig9VozZszQ66+/3iXV+9lnn9U+++xj9ey++eabGj9+vLW982J86Utf0re//e0uWQHJycnWRQnDFCC75pprNHbsWOuYu+22m+66664Oz3nvvfe07777Wu/NtM/0ardnPtdJkyZZxzXB97/+9a8Oj+/sM7SVv1Sq39R2P22sdPjzkXm9n5kpvfddaeoV0vRrbWvisI5UP6xq0LamkE4cn6G3yv12NwcAAABAH6Wnp1uLGR98wAEHdJ9m3OKnP/2pbr31Vv3+97+3eohNsH7++efr9ttv18EHH6w1a9bosssus/a94YYbFAqFdNppp2n06NFasmSJNXb4yiuv7PbY119/vX79619rcvEoa/3sc8/X6qWPRXqi/RtM3/RO38sPfvADq20mMDXTnp144olau3atcnNzW/cxheLM65gLBDk5OVq6dKnV422Y2zPOOKO1B//SSy+1gu7f/OY3rZ/Lv//9bxUWFloBuWHe/+LFi63PwFwsMK+3ZUvHzAbzfswxRo4cqW984xu6+OKLW1P3H3/8cV1xxRVWu+fPn6+nn35aF110kYqKiqyLEH35DIfE/Nd2fN8YOVc6+m3Fipjp6e6rrQ1BvbbRpxOLM+Ts5XQC5ipQ+7L0pkw9AAAAAPuYoNYUKjOp5aY3ed68efrRj36kDz/8sMu+55xzjhUQmoDVjP82vdomiL3gggusbUceeaRuuukm/fWvf7X2N1W4P/30U917771WQGp6a2+55ZZu23H11Vfr+CMP1JQxDt14zaUqWb9Jq9eaYNvE282RMcJNO64hZQJkkyq/++67W73Hpip3515nM27atNP0LI8YMcIKhM0YdrP88pe/1KZNm/Too49a+5pgN9qbH2U+qwsvvNDqDTfjzB966CHdfffdVsV38xkcccQR1hj09kxWwKGHHmpdDDCf16JFi9TQ0GA9Zi4AmON9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",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Filtrujemy filmy z lat 2010-2016 włącznie\n",
    "filtered = merged[(merged['release_year'] >= 2010) & (merged['release_year'] <= 2016)]\n",
    "\n",
    "# Grupujemy po roku i liczymy średni przychód i średni budżet\n",
    "grouped = filtered.groupby('release_year')[['revenue', 'budget']].mean().reset_index()\n",
    "\n",
    "# Tworzymy wykres\n",
    "fig, ax1 = plt.subplots(figsize=(10,6))\n",
    "\n",
    "# Wykres kolumnowy - średni przychód\n",
    "ax1.bar(grouped['release_year'], grouped['revenue'], color='skyblue', label='Średni przychód')\n",
    "ax1.set_xlabel('Rok wydania')\n",
    "ax1.set_ylabel('Średni przychód', color='skyblue')\n",
    "ax1.tick_params(axis='y', labelcolor='skyblue')\n",
    "\n",
    "# Druga oś y - średni budżet\n",
    "ax2 = ax1.twinx()\n",
    "ax2.plot(grouped['release_year'], grouped['budget'], color='orange', marker='o', label='Średni budżet')\n",
    "ax2.set_ylabel('Średni budżet', color='orange')\n",
    "ax2.tick_params(axis='y', labelcolor='orange')\n",
    "\n",
    "# Formatowanie osi X jako całkowite lata\n",
    "ax1.set_xticks(grouped['release_year'])\n",
    "ax1.set_xticklabels(grouped['release_year'].astype(int))\n",
    "\n",
    "# Dodaj tytuł\n",
    "plt.title('Średni przychód i budżet filmów (2010-2016)')\n",
    "\n",
    "# Dodaj legendę poza obszarem osi (prawy górny róg)\n",
    "fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7c538a46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Najczęstszy gatunek to: Drama\n",
      "Liczba filmów w tym gatunku: 1207\n"
     ]
    }
   ],
   "source": [
    "# Zliczamy liczbę filmów w każdym gatunku\n",
    "genre_counts = merged['genre_name'].value_counts()\n",
    "\n",
    "# Wyświetlamy najczęstszy gatunek i liczbę filmów\n",
    "most_common_genre = genre_counts.idxmax()\n",
    "most_common_count = genre_counts.max()\n",
    "\n",
    "print(f\"Najczęstszy gatunek to: {most_common_genre}\")\n",
    "print(f\"Liczba filmów w tym gatunku: {most_common_count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "da8d73f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gatunek z największym średnim czasem trwania to: History\n",
      "Średni czas trwania: 133.96 minut\n"
     ]
    }
   ],
   "source": [
    "# Grupowanie i obliczanie średniego czasu trwania filmów\n",
    "avg_runtime_by_genre = merged.groupby(\"genre_name\")[\"runtime\"].mean().sort_values(ascending=False)\n",
    "\n",
    "# Najdłuższy średni czas trwania\n",
    "longest_runtime_genre = avg_runtime_by_genre.idxmax()\n",
    "longest_runtime_value = avg_runtime_by_genre.max()\n",
    "\n",
    "print(f\"Gatunek z największym średnim czasem trwania to: {longest_runtime_genre}\")\n",
    "print(f\"Średni czas trwania: {longest_runtime_value:.2f} minut\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "604418d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjMsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvZiW1igAAAAlwSFlzAAAPYQAAD2EBqD+naQAAV0BJREFUeJzt3QmcVmXdB/xrBpBFxV1IQTQ1RBHcMtHnwSXA7VGxMh+0XHJ5Kk0R06I0RSott8w1c21BExM1cyMVyARTRFxSciFxAVRUkEVE5n4///O+97wzwwzMwBzmnpvv9/M5MPe5t+uc695+51pORaFQKCQAAACg2VU2/0MCAAAAQegGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwBAM1i8eHH6+c9/nh566KGWLgoAJUToBmgFttxyy3Tccce1dDFgle2zzz7Z0pwuvvji9PnPfz61adMm7bTTTvW+Z8aNG5cqKiqy//MybNiw9Mc//jF96UtfSq1VHvUDsKYTugFWs1tuuSX78f/000/Xe3384O3du/cqP8/999+fzj///FV+HErLE088kdXrRx991NJFKQkPP/xwOvvss9Nee+2Vbr755qyluSXccccd6e67704PPPBAWn/99VMpKB5ouPPOO+u9Pg5KrLPOOqv8PF6TAMvXdgXXA1ACpk2bliorK5scuq+++mrBu8xEwBkxYkQWmEol3DU1JDenRx99NHtv3HjjjWmttdZapffMyioUCumtt97KAvcWW2yRWrOVqZ/W/poEyJvQDdAKtG/fPrU2CxYsSGuvvXZLF2ONVlVVlT799NPUoUOHVCpqBuPm8O6776aOHTsu87ir8z0TrcnRtbwcNHf9rMqBjE8++SSrW4DWTvdygFag7vjUJUuWZC1L2267bRaoNtpoo/Rf//VfaezYsdn1cdto5S4GguJSMxCfeeaZqXv37lk46dmzZ7rkkkuyH7o1LVq0KJ122mlp4403Tuuuu2469NBD09tvv509Vs0W9Pg71v3rX/9KRx11VNpggw2y8oTnnnsuK0+MuY2ydu3aNX3rW99Kc+bMqfVcxcf497//nb7xjW+k9dZbL22yySbp3HPPzcr15ptvpsMOOyx17tw5e4xLL7200fvvD3/4Q9p9991Tp06dsrL179+/ukWv+Lz1LTX3eeyfPffcM9vXEQR23XXXervtRh3EtkeLX3TdjX37ox/9aJnhBf/5z39q3a8xY46jrGeddVb291ZbbVVdzuJjxd+nnnpqNq54hx12yOr2wQcfTLvsskv6yle+Uuuxdtxxx+z2UT9Ff/rTn7J1L730Unb5jTfeSN/97nezbYhtjm0/4ogjlil7cZv+8Y9/ZOEz6i0OuBx++OHpvffeW+6Y4Tgo8JOf/CTbn1Hncb///u//To899lhakXjO6FIer+fivoiyNHYehOJQjtgHe++9d/b62Gabbarrdfz48dn47Nj22Ad/+9vflnmMKVOmpAMPPDB7XUZ9f/nLX06TJk2qvj66XMdY81//+tfV695///2sFT72Z8333He+853stV1qY7qvvPLK7PVUfP/stttuadSoUY16TX722Wdp5MiRaeutt85ej1Ev8X6ISedqivX/8z//k01CF48f+/w3v/lNVi99+/att6xRJ/vvv39OewKg+WjpBmghc+fOzX581xWBekXih+6FF16YTjzxxCxMzps3Lxsj/swzz6SBAwem//u//0vvvPNOFgB///vf17pv/MiP8Byh5oQTTsgmnoofuvHDOQL15ZdfXn3bCC0xVvWb3/xm2mOPPbIQcvDBBzdYrghkcSAgxtUWw0SU4fXXX0/HH398FihefPHFdP3112f/RzipeTAgHHnkkalXr17poosuSn/961/TT3/607ThhhtmP8D322+/9Itf/CILld///vfTF7/4xSxAL08cnIj9FYH5ggsuyFrynnzyyaxb8qBBg7IwGkGrpsmTJ6df/epXadNNN61ed8UVV2T77eijj86C4u23355t73333Ve9T2KbIjj06dMne64IGa+++moWRptDlDUOStx2221ZPcXBkBAhtyi2K+oswndcH2EmQmzcp+iDDz7IyhrB7+9//3tW3hB/x2PF/g9PPfVU1nX4f//3f1O3bt2yIHXttddmoSwOsEQIq+l73/teFsrOO++87LaxD6McEeYbEq/dG264IQ0ZMiSddNJJ6eOPP866ikeY+uc//1k9MVp94rUdr6W4XTxGiHpuig8//DCrs9jGqM/Yvvg7XmNDhw5N3/72t7MDSTFZ29e+9rXs4E8cgAqxD2PfRuCOceXt2rXLXqexf4qBPQ6+RLCfMGFCdgArPP7449nrPuoh9mME2uL+j8drbrFP6/usqRt86/Pb3/42K3ds++mnn561PsdBingPxX5Z0WsyPqNuvfXW7P5xoC/uF59dcWBnzJgxtZ4rhgTE6yA+v+K1EKE6DmTE3y+88EKtuS7itRnPe8455zTDHgLIWQGA1ermm2+ONLrcZYcddqh1nx49ehSOPfbY6st9+/YtHHzwwct9nlNOOSV7rLruvvvubP1Pf/rTWuu/9rWvFSoqKgqvvvpqdnny5MnZ7YYOHVrrdscdd1y2/rzzzqteF3/HuiFDhizzfAsXLlxm3W233ZbdfsKECcs8xsknn1y97rPPPit069YtK9dFF11Uvf7DDz8sdOzYsdY+qc8rr7xSqKysLBx++OGFpUuX1rquqqqq3vu89957hS222KKw4447FubPn9/gdnz66aeF3r17F/bbb7/qdZdffnm2DfEYK6r/6dOn11r/2GOPZevj/+W5+OKL671/iPWxvS+++GKt9aNHj86u+9e//pVdvvfeewvt27cvHHrooYUjjzyy+nZ9+vTJ9lVD2xwmTpyYPdbvfve7ZbZpwIABtfbrGWecUWjTpk3ho48+ql639957Z0vNOl68eHGt54j67dKlS+Fb3/pWYUXiNbD22msvs77ue6a+/RvliHWjRo2qXvfyyy9X78dJkyZVr3/ooYey9bGtRYMHDy6stdZahddee6163TvvvFNYd911C/3796/1XoztKRo2bFh2/aabblq49tprs3Vz5szJXudXXHFFobkUt3l5S919V7d+DjvssGU+jxr7mnz22Wez9SeeeGKt9d///vez9Y8++mit+op1Dz74YK3bxmunQ4cOhR/84Ae11p922mlZ2Wu+RwFKle7lAC0kun9HK3DdpdjquDzRehatbK+88kqTnzcmWIvursVWt6JohYrcFpNBheiWHKJ7cd3WzIZEq2BdNcdkRitZtLhFq3mIlvm6omWsKMoZXU2jXNEqX3P7oxUsWtCXJ2aTjnHN0X257qRadVvYw9KlS7OWtmgZjFa4mmPSa25HtI5GT4Volay5DcVJpO65557seVtCdMfdfvvta60rtp5Ga2uxRTV6CUSviPi72A06WhNrtrTW3ObogRFDAqJXQGxnfXV38skn19qv8VixT6ObekOijovjiGOfRetvdEmOeq/vOZpbtKRGy3ZRvK5i+6K1v+apv4p/F19zsV0xRGHw4MHZ0Imiz33uc1kLcLRmRyt+cT/Mnj07a8kNsc+jh0asL+7/uH28zvNo6Y7Xf32fNdHTY0ViX8QkcdGyvDKfNaHuePf4rAnRk6Wm6J5et7t4DDmIYSXRkl7sPRP7PnpPxL43bwTQGgjdAC0kuoUPGDBgmSW6565IdF2OkPSFL3whG5sbXcNrjs1dnghAm222WXUX2aJil+JiQIr/I6jGD+Ga6nbFrqnubUOEqOiW2qVLlyzERbfT4u0iuNZVd/bn+NEdY8GL3VZrro/wuzyvvfZatg11Q2hDoqtqdM+O8aoxBrWm6EYeBwuiLNHdPbYjuiLX3IboGh+nrooDB7G9Eeaiq/fqDOD11UGUJbr9FwNesRtzBL8YhhBBMrrARzlrhr4Y0x+BrTj2P+ogtjtee42pu+JreUX1FN2P42BTcX6CeI4IZPU9R3OLbvN1D8DEayu2ue66mtsSY9UXLlyYhfS64r0U+zK6oofiPo39HuPPYxx4cf/XrJPopt7Q+OUQwxpmzZpVa4kAuiLxGVHfZ00cIFiRH/zgB9mBifi8itfQKaec0ujhEsXPkLqfGTHMJMJ83YMx9b12wzHHHJNmzJhRva9ibH0cxIhhLwCtgdAN0ArFj/UIlDfddFM2zjHGs8ZkWcVxrS2lvpmGv/71r2fjQqMV/K677spaB4ut6PWF0Wj5bMy6UHfit1URreIxXjwOaBxwwAG1rosf+zGeO0LhNddck7XgRUthtGjWLENsf7QmRyiIQBAHQiKIR4tyMRzV18IeGhOeGqOh2Z5jcrfYjgjSMWY9Ql+8diL8xPpYIlztvPPOtXo1/OxnP8vqMA4eRN3FdkcwbmzdraieYpK7mDsgDnLEWO54bcRzxPj91XGwoqEyN+drLg5yRaCM18bEiROzx+jXr19WBxHMI3zG/o/x6Ms7zVmMr4+gXHMpBvu8xAGEaKGPOQziNfTnP/85+z/G7TdWQ6/5xr52o/U7DhzFayXE/xHc48ABQGtgIjWAVipaW2Nysljmz5+fBfGYMKzYPbuhH7o9evTIQmF0oa7Z2v3yyy9XX1/8P0LP9OnTsxauopgYrLGiVfCRRx7JJjOLFtOilekWvzIiyMU2xGRVy5uQKyZkOvbYY7PuqjVnGi+KoBGBOyacq3kqqpg5u64ITTGDdSyXXXZZNqncj3/842ziupo9GaK1uKbldcFemQBTVwS8KG+Epwj4xYBXDOMxsVWsqxk2Yxbv2C81Z4qPIQJ1y74q4jmie3YckKm5bU0JdS0hWuNjIrlil/Ga4r0U+7Zma3ns/wjdEb7jtRjvvWjVjhb0ONAQXenjfbI8cfviGQqKVsds59GFOw4exRKt7TF5WhyMGT58ePa+WN5nTbz/4v1e7EkTopU6XkPFz5oViddkHOCKmenjwFgcIIvJ1Ro6MAJQarR0A7RCdU+3FS2U0YWz5mzExbGOdQPSQQcdlIWuq666qtb6mHk4fjzH6Y9CcWxltOzWPX1QYxV/FNdtHYxZrVeHCNERfqL1um6rabFMccAiTm21+eabZ92c6wsQsR2xvmZrdMzOHT/+63alr6sY9ot1U+y2XhxfHeJxYxbuxmioXlek2MU5Qkt05S52l471cWAkZr+vO544trtu3UX9N1erfPE5Qs3niRmuo0W4lEW5Y0x0jN+veQq1CJQxPCEOZkR38aLYt3G7GItc3M/x2owDHXFwJsbMr2g8dxywqdtFPO9zsNf9rInx9zFcI+qreKaF5X3W1Pd+j+0NyzsTQl3RcyQO4sXM5vGejdMKArQWWroBWqH40RunJYpzG0eLdwSmaDGM0zMVxXUhJkyLAB0hIcYYH3LIIWnffffNWl8jBETrWXQbjvAQp0gqhsK4/1e/+tXsB3P88C6eMixahRvb4hqhI1rgf/nLX2Y/0CPYxnNF6/nqEAciYjvjPMERaKKFLlqqY1Ko6PIbpy6K1sVoCY/x3LEPaop9Ed2AIxxEUIhu59Hi9u6772YT4cXj1xxLH+E+wnTcPlrx4nZx0CLGDRfPWx6nh4p9Ga2EEdKj/qL1OSYPa4xivcZ2RX3GaaqiTlc0oVSUNVpFo2W25mR4UT8xbjfUDX1xKq04LVcE9HjNRRCOXhLRvby5xHNEK3cc+Ij9Fq+N6667Lnu+CFelLE5nVzwve0w42LZt2+yUYXGAJV7zNRX3bez/6P1Qc//H5IXxuozJ7UpNHFiI103MVRBdvKNHRBywi7oq9pRp6DUZny3RUyIOKEUgj0n+4vRucXArDojF51BjxbCHGA4xevTorNU8htMAtBZCN0ArFEH63nvvzQJs/MCPgBcBICZUK4qAGeEqAl2MgYyWqfhBHK1rcd/o7h2tbtHlOM7lHOchLs4qXPS73/0u+8EdMwfHbN7Rshb3icmjGtvCFq1+UY4IqVGG+BEfISNC7+oQQTi69EYLbYSC6BIcLb3FSZhiQqwQ+6+uCAwRumN8cYw3jnOHx4GJeLxoMY6DFjVDd4z7jnUx1j5maY+JxyJoRLAvtiyHOAd0tNjF48WY6piZPQJIjP1ekQhmcRAhgml0Sy4OAWjMLM4R/CK0FA8AFANT7JMI/TVn6y6emzwO1kR5o1t5BK8I3XVnmF4VMZ47JgSLsBrd9yNsx+s1yjlu3LhUyuIASnTNjwMocQAn6iL2YZS/7r6M90yc9z0OxNTc/8UwHhOV1Ry6UCridRr1Hwed4iBIHECKz5+a58de3msy5pmI4QPRNTw+Q+LzJPbXygwfiAnV4nzoJlADWpuKOG9YSxcCgNbj2WefzVqdIlgcffTRLV0cYA0RB4HOOOOM7MBW3ZnyAUqZMd0ANChmuq4ruptHa3l0iwVYHaKNKHqbRM8RgRtobXQvB6BBMS41Ti8VXZ9jvGp0C4/l5JNPXuY8xgDNLc5rHsNhYvb/559/fpl5FwBaA93LAWhQTBJVnGgsxnNGC1OMp4yx0RHCAfIUXcljDoWY+yAmq4tTlQG0NkI3AAAA5MSYbgAAAMiJ0A0AAAA5EboBAAAgJ2vcLDhVVVXpnXfeSeuuu26qqKho6eIAAADQCsX0aB9//HHabLPNstOpNmSNC90RuJ3mBgAAgObw5ptvpm7dujV4/RoXuqOFu7hjOnfuvNKPs2TJkvTwww+nQYMGpXbt2jVjCWlp6rY8qdfypW7Lk3otX+q2PKnX8qVuGzZv3rysQbeYMRuyxoXuYpfyCNyrGro7deqUPYYXX3lRt+VJvZYvdVue1Gv5UrflSb2WL3W7YisatmwiNQAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEC5h+6LLrooVVRUpKFDhy73dqNHj07bbbdd6tChQ9pxxx3T/fffv9rKCAAAAK0udD/11FPpN7/5TerTp89yb/fEE0+kIUOGpBNOOCFNmTIlDR48OFteeOGF1VZWAAAAaDWhe/78+enoo49Ov/3tb9MGG2yw3NteccUV6YADDkhnnXVW6tWrVxo5cmTaZZdd0lVXXbXaygsAAACtJnSfcsop6eCDD04DBgxY4W0nTpy4zO3233//bD0AAACUmrYt+eS33357euaZZ7Lu5Y0xa9as1KVLl1rr4nKsb8jixYuzpWjevHnZ/0uWLMmWlVW876o8BqVJ3ZanUq7Xt956K82ZMyeVsvgcbd++fSpFVVVV2f8x7GiTTTZJ3bp1a+kiUebvWVaNui1P6rV8qduGNXaftFjofvPNN9Ppp5+exo4dm02KlpcLL7wwjRgxYpn1Dz/8cOrUqdMqP36Un/KkbsuTei1fM2fOzJbnnnuupYtCM/KeLV/qtjyp1/Klbpe1cOHCVNKhe/Lkyendd9/NxmQXLV26NE2YMCEbox2tKm3atKl1n65du6bZs2fXWheXY31Dhg8fnoYNG1arpbt79+5p0KBBqXPnzqt0VCNeeAMHDkzt2rVb6ceh9Kjb8lSq9Tp16tTUv3//dPi5l6dNemydStErk8anx264tGTL2CYVUv+1F6a7Xp6dRo8Ymn2P9O3bt6WLRZm+Z1l16rY8qdfypW4bVuxFXbKh+8tf/nJ6/vnna607/vjjs9OB/eAHP1gmcId+/fqlRx55pNZpxeIFEOsbEt0h6+sSGS+Y5njRNNfjUHrUbXkqtXqtrKxMixYtShv22CZ17VWaQXHm9FdLuoyVVZ+l9NaTaYPun8/KGfu0lOqY8nrP0nzUbXlSr+VL3S6rsfujxUL3uuuum3r37l1r3dprr5022mij6vXHHHNM2nzzzbMu4iG6o++9997p0ksvzSZfizHhTz/9dLr++utbZBsAAACgpGcvX54ZM2Zk4/OK9txzzzRq1KgsZEfXwTvvvDPdfffdy4R3AAAASGv67OV1jRs3brmXwxFHHJEtAAAAUOpKuqUbAAAAWjOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAUI6h+9prr019+vRJnTt3zpZ+/fqlBx54oMHb33LLLamioqLW0qFDh9VaZgAAAGistqkFdevWLV100UVp2223TYVCId16663psMMOS1OmTEk77LBDvfeJcD5t2rTqyxG8AQAAoBS1aOg+5JBDal3+2c9+lrV+T5o0qcHQHSG7a9euq6mEAAAAUAZjupcuXZpuv/32tGDBgqybeUPmz5+fevTokbp37561ir/44ourtZwAAADQKlq6w/PPP5+F7E8++SSts846acyYMWn77bev97Y9e/ZMN910UzYOfO7cuemSSy5Je+65Zxa8o6t6fRYvXpwtRfPmzcv+X7JkSbasrOJ9V+UxKE3qtjyVar1WVVWljh07pjapkCqrPkulqG1lRUmXsVimKF+UM/ZpqdUz5fOeZdWp2/KkXsuXum1YY/dJRSEGU7egTz/9NM2YMSML0XfeeWe64YYb0vjx4xsM3nU3slevXmnIkCFp5MiR9d7m/PPPTyNGjFhm/ahRo1KnTp2aZRsAAABYsyxcuDAdddRRWZaNucdKNnTXNWDAgLT11lun3/zmN426/RFHHJHatm2bbrvttka3dEfX9Pfff3+5O6YxgX/s2LFp4MCBqV27div9OJQedVueSrVep06dmvr3759OvuHetFnP3qkUTX34njRm5BklW8Zo6d72nclpwoJO6doTD0sTJkxIffv2beliUabvWVadui1P6rV8qduGRbbceOONVxi6W7x7eV3RLbBmSF7ROPDonn7QQQc1eJv27dtnS13xgmmOF01zPQ6lR92Wp1Kr18rKyrRo0aK0NFWkqsqS+0jOfFZVKPkyhihflDP2aSnVMeX1nqX5qNvypF7Ll7pdVmP3R4v+eho+fHg68MAD0xZbbJE+/vjjrMv3uHHj0kMPPZRdf8wxx6TNN988XXjhhdnlCy64IO2xxx5pm222SR999FG6+OKL0xtvvJFOPPHEltwMAAAAKL3Q/e6772bBeubMmWm99dbLJkiLwB1dF0KM9Y4Wi6IPP/wwnXTSSWnWrFlpgw02SLvuumt64oknGjX+GwAAANao0H3jjTcu9/po9a7p8ssvzxYAAABoDUrmPN0AAABQboRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAOYbua6+9NvXp0yd17tw5W/r165ceeOCB5d5n9OjRabvttksdOnRIO+64Y7r//vtXW3kBAACg1YTubt26pYsuuihNnjw5Pf3002m//fZLhx12WHrxxRfrvf0TTzyRhgwZkk444YQ0ZcqUNHjw4Gx54YUXVnvZAQAAoKRD9yGHHJIOOuigtO2226YvfOEL6Wc/+1laZ5110qRJk+q9/RVXXJEOOOCAdNZZZ6VevXqlkSNHpl122SVdddVVq73sAAAA0GrGdC9dujTdfvvtacGCBVk38/pMnDgxDRgwoNa6/fffP1sPAAAApaZtSxfg+eefz0L2J598krVyjxkzJm2//fb13nbWrFmpS5cutdbF5VjfkMWLF2dL0bx587L/lyxZki0rq3jfVXkMSpO6LR9vvfVWmjNnTvZ3VVVV9n8MTamsLJnjjWnatGmpY8eOqU0qpMqqz1IpaltZUdJlLJYpyhfljLr2/m39fBaXL3VbntRr+VK3DWvsPqkoFAqF1II+/fTTNGPGjDR37tx05513phtuuCGNHz++3uC91lprpVtvvTUb1110zTXXpBEjRqTZs2fX+/jnn39+dn1do0aNSp06dWrmrQEAAGBNsHDhwnTUUUdlWTYmBi/Zlu4I0ttss03296677pqeeuqpbOz2b37zm2Vu27Vr12XCdVyO9Q0ZPnx4GjZsWK2W7u7du6dBgwYtd8c05qjG2LFj08CBA1O7du1W+nEoPeq2PEydOjX1798/HX7u5WmTHltnraD9116YJizolJamilQqXpk0Pj12w6Xp5BvuTZv17J1K0dSH70ljRp5RsmWMlu5t35mc1e21Jx6WJkyYkPr27dvSxWIV+SwuX+q2PKnX8qVuG1bsRb0iLR6664pugTW7g9cU3dAfeeSRNHTo0Op18QJoaAx4aN++fbbUFS+Y5njRNNfjUHrUbesWXcgXLVqUNuyxTeraq+//2wX5rSdTl547pqrK0vnomzn91ayccSCglMpV02dVhZIvY4jyRTmj7r13y4fP4vKlbsuTei1f6nZZjd0fLfrrKVqhDzzwwLTFFlukjz/+OOvyPW7cuPTQQw9l1x9zzDFp8803TxdeeGF2+fTTT0977713uvTSS9PBBx+cTbwWpxq7/vrrW3IzAAAAoPRC97vvvpsF65kzZ6b11lsv9enTJwvc0XUhxFjvmhMe7bnnnlkwP+ecc9KPfvSj7FRjd999d+rdu/S6OwIAAECLhu4bb7xxuddHq3ddRxxxRLYAAABAqSud8+YAAABAmRG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAA5Ri6L7zwwvTFL34xrbvuumnTTTdNgwcPTtOmTVvufW655ZZUUVFRa+nQocNqKzMAAAC0itA9fvz4dMopp6RJkyalsWPHpiVLlqRBgwalBQsWLPd+nTt3TjNnzqxe3njjjdVWZgAAAGistqkFPfjgg8u0YkeL9+TJk1P//v0bvF+0bnft2nU1lBAAAADKZEz33Llzs/833HDD5d5u/vz5qUePHql79+7psMMOSy+++OJqKiEAAAC0kpbumqqqqtLQoUPTXnvtlXr37t3g7Xr27Jluuumm1KdPnyykX3LJJWnPPffMgne3bt2Wuf3ixYuzpWjevHnZ/9GVPZaVVbzvqjwGpUndlof4TOnYsWNqkwqpsuqzbAnF/0tF28qKWuUsRaVexmKZonxRzqh779/Wz2dx+VK35Um9li9127DG7pOKQqFQSCXgO9/5TnrggQfS448/Xm94Xt6G9urVKw0ZMiSNHDlymevPP//8NGLEiGXWjxo1KnXq1GmVyw0AAMCaZ+HChemoo47KGoNj3rGSDt2nnnpquueee9KECRPSVltt1eT7H3HEEalt27bptttua1RLd3RLf//995e7YxoT9mPyt4EDB6Z27dqt9ONQetRteZg6dWo2N8TJN9ybNuvZO2sN3fadyemVzXZNVZUl08knTX34njRm5BnV5SxFpV7GYt1OWNApXXviYdl3Sd++fVu6WKwin8XlS92WJ/VavtRtwyJbbrzxxisM3U3+5bnFFlukffbZJ+29997Z/1tvvXVaWZH3v/e976UxY8akcePGrVTgXrp0aXr++efTQQcdVO/17du3z5a64gXTHC+a5nocSo+6bd0qKyvTokWL0tJUUStkx9+lFLo/qyrUW85S0hrKGKJ8Uc6oe+/d8uGzuHyp2/KkXsuXul1WY/dHkydS+/nPf56dF/sXv/hF2nbbbbNW42984xvpt7/9bXrllVea9FhxurA//OEPWVfvOFf3rFmzsiV+NBUdc8wxafjw4dWXL7jggvTwww+n119/PT3zzDPZc8cpw0488cSmbgoAAADkqslNFhFyYwlxjuw41/Z9992Xvvvd72aT10TLc2Nde+212f/RYl7TzTffnI477rjs7xkzZmStFkUffvhhOumkk7JwvsEGG6Rdd901PfHEE2n77bdv6qYAAABArtqu7IDxmPAsuoQ/9thjacqUKdmM43XD84o0Zjh5PEdNl19+ebYAAABA2YXuOD1XhOyYMTxC9g9/+MNssqJodQYAAABWYUz3yy+/nNZee+203XbbZUuEb4EbAAAAmiF0z5kzJz366KNpjz32SA899FDaa6+90uabb56dnywmUwMAAABWMnRXVFSkPn36pNNOOy3deeed6YEHHsjO2TZ69Oj07W9/u6kPBwAAAGWryWO64zRdMblZLDGZ2scff5x23HHH7Hzbce5uAAAAYCVD9+6775523nnnLGDHqbtiErX11luvqQ8DAAAAZa/JofuDDz5InTt3zqc0AAAAsCaH7mLgnjx5cnrppZeyv7fffvu0yy67NH/pAAAAoJxD9+LFi1P79u2rL7/77rvpyCOPTOPHj0/rr79+tu6jjz5K++67b7r99tvTJptskm+JAQAAoFxmL7/sssvS7373u+rLMWHa/Pnz04svvph1NY/lhRdeSPPmzctmNAcAAAAa2dL99a9/PX3ta19Lb7zxRjr33HPTgw8+mP72t7+lXr16Vd8mupdfffXVadCgQSt6OAAAAFhjrLCle+utt04TJ05Mb775Zna5qqoqtWvXbpnbxbq4DgAAAGhk6A4dOnRI119/ffb3fvvtl04//fT0zjvvVF//9ttvpzPOOCN9+ctfbszDAQAAwBqhUaG7pquuuiobv73llltmreCxbLXVVtm6K6+8Mp9SAgAAwJpwyrDu3bunZ555JhvX/fLLL2frYnz3gAED8igfAAAArDmhO1RUVKSBAwdmCwAAANCMofupp55Kjz32WHbO7rqTp8UpxgAAAICVCN0///nP0znnnJN69uyZunTpkrV6F9X8GwAAANZ0TQ7dV1xxRbrpppvScccdl0+JAAAAYE2dvbyysjLttdde+ZQGAAAA1uTQHefjvvrqq/MpDQAAAKzJ3cu///3vp4MPPjg7P/f222+f2rVrV+v6u+66qznLBwAAAGtO6D7ttNOymcv33XfftNFGG5k8DQAAAJordN96663pz3/+c9baDQAAADTjmO4NN9ww61oOAAAANHPoPv/889N5552XFi5c2NS7AgAAwBqlyd3Lf/3rX6fXXnstdenSJW255ZbLTKT2zDPPNGf5AAAAYM0J3YMHD86nJAAAALCmh+7oWg4AAADkMKYbAAAAaMaW7g022KDR5+P+4IMPGvnUAAAAUN4aFbp/9atf5V8SAAAAWBND97HHHpt/SQAAAGBNDN3z5s1LnTt3rv57eYq3AwAAgDVdo0L3+uuvn2bNmpU23XTT7O/6xncXCoVs/dKlS/MoJwAAAJRn6H7sscfShhtuWP03AAAA0Eyh+4orrkg777xz1nX8jTfeSEceeWRq3759Y+4KAAAAa6xGnaf7vvvuSwsWLMj+Pv7449PcuXPzLhcAAACsGS3d2223XRo+fHjad999s7Hbd9xxR4MTph1zzDHNXUYAAAAo39B93XXXpWHDhqW//vWv2WRp55xzTr2TqcU6oRsAAACaELr33HPPNGnSpOzvysrK9O9//zubyRwAAABYxTHdNU2fPj1tsskmTb0bAAAArHEa1dJdU48ePfIpCQAAAKzpLd0AAABA4wjdAAAAkBOhGwAAAHIidAMAAECpTKQW7rzzznTHHXekGTNmpE8//bTWdc8880xzlQ0AAADWrJbuX//61+n4449PXbp0SVOmTEm777572mijjdLrr7+eDjzwwHxKCQAAAGtC6L7mmmvS9ddfn6688sq01lprpbPPPjuNHTs2nXbaaWnu3LlNeqwLL7wwffGLX0zrrrtu2nTTTdPgwYPTtGnTVni/0aNHp+222y516NAh7bjjjun+++9v6mYAAABA6YXu6FK+5557Zn937Ngxffzxx9nf3/zmN9Ntt93WpMcaP358OuWUU9KkSZOy4L5kyZI0aNCgtGDBggbv88QTT6QhQ4akE044IWtpj6AeywsvvNDUTQEAAIDSCt1du3ZNH3zwQfb3FltskQXmMH369FQoFJr0WA8++GA67rjj0g477JD69u2bbrnllizUT548ucH7XHHFFemAAw5IZ511VurVq1caOXJk2mWXXdJVV13V1E0BAACA0grd++23X7r33nuzv2Ns9xlnnJEGDhyYjjzyyHT44YevUmGK3dM33HDDBm8zceLENGDAgFrr9t9//2w9AAAAtOrZy2M8d1VVVfZ3dA2PSdSiy/ehhx6a/u///m+lCxKPOXTo0LTXXnul3r17N3i7WbNmZZO41RSXY319Fi9enC1F8+bNy/6PruyxrKzifVflMShNLVm3b731VpozZ04qdfGeat++fSplMT9EDIFpkwqpsuqzbAnF/0tF28qKWuUsRaVexmKZonxRzpdeeqn6e6pUtYb3UIjv+G7durXIc/ueLV/qtjyp1/KlbhvW2H1SUWhqn/CcfOc730kPPPBAevzxx5f7BR+Tt916663ZuO6ak7uNGDEizZ49e5nbn3/++dl1dY0aNSp16tSpGbcAAACANcXChQvTUUcdlfXY7ty5c/Oep/vDDz9MN954Y9aaELbffvusq/nyuoUvz6mnnpruu+++NGHChBUeUY8x5XXDdVyO9fUZPnx4GjZsWK2W7u7du2cTti1vxzTmqEZM/hZd69u1a7fSj0Ppaam6nTp1aurfv386/NzL0yY9tk6l6pVJ49NjN1zaasp58g33ps169s5aQ7d9Z3J6ZbNdU1XlSn305WLqw/ekMSPPqC5nKSr1Mhbr9q6XZ6fRI4a2mtdmqZfzvTdey+o9vptj3pXVzfds+VK35Um9li9127BiL+oVafIvz/jyja7kEVh322236nN3X3DBBekvf/lLFhoaKxrZv/e976UxY8akcePGpa222mqF9+nXr1965JFHsq7oRfEiiPX1ie579XXhixdMc7xomutxKD2ru24rKyvTokWL0oY9tklde63+H7iNNXP6q62qnEtTRa2QHX+XUuj+rKpQbzlLSWsoY81ytpbXZqmXM+o7yhmfTS35Ped7tnyp2/KkXsuXul1WY/dHk389xTjur3/96+naa69Nbdq0ydYtXbo0ffe7382ue/7555v0WNHN+5577snO1V0cl73eeutl4/LCMccckzbffPPsnN7h9NNPT3vvvXe69NJL08EHH5xuv/329PTTT2djzQEAAKBVz17+6quvpjPPPLM6cIf4O7pwx3VNEcE9+r/vs88+6XOf+1z18qc//an6NnEKsZkzZ1ZfjnOER1CPkB3d3e6888509913L3fyNQAAAGgJTW7pjnNix1junj171lof65o65qsxc7hFt/O6jjjiiGwBAACAVh+6n3vuueq/TzvttKyLd7Rq77HHHtm6SZMmpauvvjpddNFF+ZUUAAAAyjF077TTTqmioqJWy/TZZ5+9zO1iuvQjjzyyeUsIAAAA5Ry6p0+fnn9JAAAAYE0M3T169Mi/JAAAALCmz14eM5Xvu+++6YMPPqi1fvbs2bVmNAcAAIA1XZNDd4zrXrx4cdptt93Siy++uMx1AAAAwEqG7phQ7c9//nM65JBDUr9+/dI999xT6zoAAABgFVq6oxv5FVdckS655JJstvKf/vSnWrkBAABgZSZSa8jJJ5+ctt1223TEEUekCRMmrMpDAQAAQNlpckt3zGRec8K0mFRt0qRJ6c0332zusgEAAMCa1dJd3zm7t9lmmzRlypRsBnMAAABgJVu6n3rqqfTkk08us37q1Knpvffea+rDAQAAQNlqcug+5ZRT6u1K/vbbb2fXAQAAACsZuv/1r3+lXXbZZZn1O++8c3YdAAAAsJKhu3379vWO3Z45c2Zq23aVJkMHAACANTt0Dxo0KA0fPjzNnTu3et1HH32UfvSjH6WBAwc2d/kAAACg1Wpy0/Qll1yS+vfvn506LLqUh2effTZ16dIl/f73v8+jjAAAALBmhO7NN988Pffcc+mPf/xjNmN5x44d0/HHH5+GDBmS2rVrl08pAQAAoBVaqUHYa6+9djr55JObvzQAAACwpoXue++9Nx144IFZS3b8vTyHHnpoc5UNAAAAyj90Dx48OM2aNSttuumm2d8NqaioSEuXLm3O8gEAAEB5h+6qqqp6/wYAAACa8ZRhDXnrrbeM8wYAAIA8QvecOXPSjTfe2FwPBwAAAK1es4VuAAAAoDahGwAAAHIidAMAAEBLzl4evvKVryz3+o8++qg5ygMAAABrXuheb731Vnj9Mccc0xxlAgAAgDUrdN988835lgQAAADKjDHdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAOYbuCRMmpEMOOSRtttlmqaKiIt19993Lvf24ceOy29VdZs2atdrKDAAAAK0idC9YsCD17ds3XX311U2637Rp09LMmTOrl0033TS3MgIAAMDKapta0IEHHpgtTRUhe/3118+lTAAAALBGj+neaaed0uc+97k0cODA9I9//KOliwMAAACl19LdVBG0r7vuurTbbrulxYsXpxtuuCHts88+6cknn0y77LJLvfeJ28VSNG/evOz/JUuWZMvKKt53VR6D0tRSdVtVVZU6duyY2qRCqqz6LJWqtpUVrbKcxbKWWplbw/4s9TIWy1Tq5SxqLeWM8kU547OpJb7rfM+WL3VbntRr+VK3DWvsPqkoFAqFVAJiQrQxY8akwYMHN+l+e++9d9piiy3S73//+3qvP//889OIESOWWT9q1KjUqVOnlS4vAAAAa66FCxemo446Ks2dOzd17ty5PFq667P77runxx9/vMHrhw8fnoYNG1arpbt79+5p0KBBy90xjTmqMXbs2KyLe7t27Vb6cSg9LVW3U6dOTf37908n33Bv2qxn71Sqpj58Txoz8oxWV85oUdz2ncnplc12TVWVpfPR1xr2Z6mXsVi3d708O40eMbRky9la9mfRO9NeSNefeGh2ppGY9HR18z1bvtRteVKv5UvdNqzYi3pFSueX50p69tlns27nDWnfvn221BUvmOZ40TTX41B6VnfdVlZWpkWLFqWlqaKkQmFdn1UVWnU54+9SKndr2J+toYxBOZtXlC/KGZ9NLfk953u2fKnb8qRey5e6XVZj90eLftvPnz8/vfrqq9WXp0+fnoXoDTfcMOsyHq3Ub7/9dvrd736XXf+rX/0qbbXVVmmHHXZIn3zySTam+9FHH00PP/xwC24FAAAAlGDofvrpp9O+++5bfbnYDfzYY49Nt9xyS3YO7hkzZlRf/+mnn6YzzzwzC+IxHrtPnz7pb3/7W63HAAAAgFLRoqE7Zh5f3jxuEbxrOvvss7MFAAAAWoNWeZ5uAAAAaA2EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQDmG7gkTJqRDDjkkbbbZZqmioiLdfffdK7zPuHHj0i677JLat2+fttlmm3TLLbeslrICAABAqwrdCxYsSH379k1XX311o24/ffr0dPDBB6d99903Pfvss2no0KHpxBNPTA899FDuZQUAAICmatuST37ggQdmS2Ndd911aauttkqXXnppdrlXr17p8ccfT5dffnnaf//9cywpAAAAlPmY7okTJ6YBAwbUWhdhO9YDAABAqWnRlu6mmjVrVurSpUutdXF53rx5adGiRaljx47L3Gfx4sXZUhS3DUuWLMmWlVW876o8xoq89dZbac6cOanUxf6NMfblUs6qqqrs/ylTpqTKytV3XGratGnZa7hNKqTKqs9SqWpbWdEqy1ksa6mVuTXsz1IvY7FMpV7OotZSzihf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/A21tES+g1aksWVr8U+BaIU+9thj02677ZZ233339Ktf/SotWLAgm808HHPMMVkX9AsvvDC7fMEFF6Q99tgjbbPNNumjjz5KF198cXbKsBNPPLGFtwQAAABKLHQfeeSR6b333ks/+clP0qxZs9JOO+2UHnzwwerJ1WbMmJEd4Sj68MMPs1OMxW032GCDrKU8xoTH6cYAAACglLR46A7Rlbyh7uTjxo2rdfnyyy/PFgAAACh1LXqebgAAAChnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAACAnQjcAAADkROgGAACAnAjdAAAAkBOhGwAAAHIidAMAAEBOhG4AAADIidANAAAAORG6AQAAICdCNwAAAORE6AYAAICcCN0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAAByInQDAABAToRuAAAAyInQDQAAADkRugEAAKCcQ/fVV1+dttxyy9ShQ4f0pS99Kf3zn/9c7u1Hjx6dtttuu+z2O+64Y7r//vtXW1kBAACg1YTuP/3pT2nYsGHpvPPOS88880zq27dv2n///dO7775b7+2feOKJNGTIkHTCCSekKVOmpMGDB2fLCy+8sNrLDgAAACUdui+77LJ00kknpeOPPz5tv/326brrrkudOnVKN910U723v+KKK9IBBxyQzjrrrNSrV680cuTItMsuu6SrrrpqtZcdAAAASjZ0f/rpp2ny5MlpwIAB/3+BKiuzyxMnTqz3PrG+5u1DtIw3dHsAAABoKW1b7JlTSu+//35aunRp6tKlS631cfnll1+u9z6zZs2q9/axvj6LFy/OlqK5c+dm/3/wwQdpyZIlK132uO/ChQvTnDlzUrt27VJzmzdvXjZmffa059NnC+enUvXhm6+XXTnbpELqvvaiNGPKpLQ0VZRkGVtSay1nS9VrOezPUi9jsW4/enN6SZeztezPojn/3/6Mg+PxnbS6VVVVZd+zf//737MD8g2J6+K2pU45m163DXnllVdK/j20Jr7PV7VeV8R7qHmszPunJX5Dzfn/Xpvxuoy8Vao+/vjj7P9CobD8GxZa0Ntvvx2lKzzxxBO11p911lmF3Xffvd77tGvXrjBq1Kha666++urCpptuWu/tzzvvvOw5LBaLxWKxWCwWi8ViSc28vPnmm8vNvS3a0r3xxhunNm3apNmzZ9daH5e7du1a731ifVNuP3z48GyitqI48hSt3BtttFGqqFj5IzVx1KV79+7pzTffTJ07d17px6H0qNvypF7Ll7otT+q1fKnb8qRey5e6bVi0cEdr92abbVa63cvXWmuttOuuu6ZHHnkkm4G8GIrj8qmnnlrvffr165ddP3To0Op1Y8eOzdbXp3379tlS0/rrr99s2xAvPC++8qRuy5N6LV/qtjyp1/KlbsuTei1f6rZ+6623XlqRFg3dIVqhjz322LTbbrul3XffPf3qV79KCxYsyGYzD8ccc0zafPPN04UXXphdPv3009Pee++dLr300nTwwQen22+/PT399NPp+uuvb+EtAQAAgBIL3UceeWR677330k9+8pNsMrSddtopPfjgg9WTpc2YMaPWZAx77rlnGjVqVDrnnHPSj370o7Ttttumu+++O/Xu3bsFtwIAAABKMHSH6EreUHfycePGLbPuiCOOyJaWFF3WzzvvvGW6rtP6qdvypF7Ll7otT+q1fKnb8qRey5e6XXUVMZtaMzwOAAAAUEfzn0QPAAAAyAjdAAAAkBOhGwAAAHIidK/A0qVL07nnnpu22mqr1LFjx7T11lunkSNHZidCL4q/Y/b1z33uc9ltBgwYkF555ZUWLTe1TZgwIR1yyCHZiesrKiqyGe9rakwdfvDBB+noo4/Ozk8Y53o/4YQT0vz581fzltCUul2yZEn6wQ9+kHbccce09tprZ7eJ0xC+8847tR5D3ba+92xN3/72t7PbxCkna1KvrbduX3rppXTooYdm5z6N9+4Xv/jF7GwmRZ988kk65ZRT0kYbbZTWWWed9NWvfjXNnj17NW8JTanXeO/FpLndunXLvme33377dN1119W6jXotPXHK3nj/rbvuumnTTTdNgwcPTtOmTWtyvcX7N07126lTp+xxzjrrrPTZZ5+t5q2hsfUa35/f+973Us+ePbP36xZbbJFOO+20NHfu3FqPo14bT+hegV/84hfp2muvTVdddVX2IyAu//KXv0xXXnll9W3i8q9//evsy+PJJ5/MfiDsv//+2YcQpSHO/d63b9909dVX13t9Y+owfry/+OKLaezYsem+++7LfmCcfPLJq3EraGrdLly4MD3zzDPZgbP4/6677sq+VOLHfE3qtvW9Z4vGjBmTJk2alP3Qr0u9ts66fe2119J//dd/pe222y47g8lzzz2XvYc7dOhQfZszzjgj/eUvf0mjR49O48ePzw6kfeUrX1mNW0FT63XYsGHZKWH/8Ic/ZL+nhg4dmoXwe++9t/o26rX0RD1EoI7P2fgsjYPZgwYNyuq7sfUWDVgRzD799NP0xBNPpFtvvTXdcsstWWMHpVmvUYexXHLJJemFF17I6ivev3Hwuki9NlHMXk7DDj744MK3vvWtWuu+8pWvFI4++ujs76qqqkLXrl0LF198cfX1H330UaF9+/aF2267bbWXlxWLl/2YMWOqLzemDv/1r39l93vqqaeqb/PAAw8UKioqCm+//fZq3gIaW7f1+ec//5nd7o033sguq9vWW69vvfVWYfPNNy+88MILhR49ehQuv/zy6uvUa+ut2yOPPLLwjW98o8H7xOdzu3btCqNHj65e99JLL2WPNXHixFzLy8rX6w477FC44IILaq3bZZddCj/+8Y+zv9Vr6/Duu+9mdTJ+/PhG19v9999fqKysLMyaNav6Ntdee22hc+fOhcWLF7fAVrCieq3PHXfcUVhrrbUKS5YsyS6r16bR0r0Ce+65Z3rkkUfSv//97+zy1KlT0+OPP54OPPDA7PL06dPTrFmzsu7IRdEd7ktf+lKaOHFii5WbxmtMHcb/0T11t912q75N3L6ysjJrGaf1iK5R0fUx6jOo29apqqoqffOb38y6su2www7LXK9eW2+9/vWvf01f+MIXst5G0V0xPotrdlWePHly1ipT8zM7WsWj+6Pv3dL+PRWt2m+//XY2pOuxxx7LfltF61pQr61DsXvxhhtu2Oh6i/9jmFeXLl2qbxPv73nz5mW9kSi9em3oNjFcq23bttll9do0QvcK/PCHP0z/+7//m32AtGvXLu28885Zl6jothgirIWaL7ji5eJ1lLbG1GH8Hz/+aooPnfhwUs+tRwwXiDHeQ4YMyb44grptnWKoT9RTjDGrj3ptnd59991s7O9FF12UDjjggPTwww+nww8/POuqGt0hQ9TfWmutVX3grMj3bmmLYXkxjjvGdEf9Rf1GV/T+/ftn16vX1nFQLH4D77XXXql3796Nrrf4v77fWMXrKL16rev999/P5rSqOURLvTbN/3uoggbdcccd6Y9//GMaNWpU1pry7LPPZi/MGD947LHHtnTxgEaKI/Ff//rXsxaWmKeB1itaVq644opsnH70WqC8fvyFww47LBsnGnbaaadsvGDMubH33nu3cAlZldAd40ejtbtHjx7ZHAsxpjR+T9VsJaV0RX3F+N7o8cmaU6/Rch1jt+Og2fnnn7/ay1cutHSvQHRdLLZ2RxeK6M4YPwRi1r/QtWvX7P+6szTG5eJ1lLbG1GH8Hy0wNcXsjDG7o3puPYH7jTfeyCYMKbZyB3Xb+vz973/P6iy6L0brdSxRt2eeeWbacssts9uo19Zp4403zuozftzV1KtXr+rZy6P+YuKejz76qNZtfO+WrkWLFqUf/ehH6bLLLstmOO/Tp082idqRRx6ZTdQU1Gtpi/qKCSljWED0VihqTL3F//X9xipeR+nVa9HHH3+c9UqJWc5j4tLo9VukXptG6F6BmP04xgDW1KZNm+qj8XEqsXhhxbjvmkeEYsxgv379Vnt5abrG1GH8H18o0cJW9Oijj2avgxhvSOkH7jgF3N/+9rfslCY1qdvWJw5+xozW0fOouERrWRwkfeihh7LbqNfWKbqpxmls6p6SKMb+Ruto2HXXXbMffjU/s+P2Ecp975bu53Asy/s9pV5LU/QOi2AWgSs+Q+M3U02Nqbf4//nnn691ILR4ALzuATZKo16Lv4VjzoX4XI4eKjXPIBHUaxM1ceK1Nc6xxx6bzY573333FaZPn1646667ChtvvHHh7LPPrr7NRRddVFh//fUL99xzT+G5554rHHbYYYWtttqqsGjRohYtO/+/jz/+uDBlypRsiZf9ZZddlv1dnMG6MXV4wAEHFHbeeefCk08+WXj88ccL2267bWHIkCEtuFWsqG4//fTTwqGHHlro1q1b4dlnny3MnDmzeqk5s6a6bX3v2brqzl4e1GvrrNv4no3ZkK+//vrCK6+8UrjyyisLbdq0Kfz973+vfoxvf/vbhS222KLw6KOPFp5++ulCv379soXSrde99947m8H8scceK7z++uuFm2++udChQ4fCNddcU/0Y6rX0fOc73ymst956hXHjxtX6Dl24cGGj6+2zzz4r9O7duzBo0KDsu/jBBx8sbLLJJoXhw4e30FaxonqdO3du4Utf+lJhxx13LLz66qu1bhP1GdRr0wjdKzBv3rzC6aefnn2YxJfD5z//+ez0FjV/sMcpp84999xCly5dstNMffnLXy5MmzatRctNbfElHz8C6i5xUKWxdThnzpzsB/s666yTnQ7h+OOPz35kULp1GwfK6rsulrhfkbptfe/ZxoRu9dp66/bGG28sbLPNNtn3bt++fQt33313rceIA6Lf/e53CxtssEGhU6dOhcMPPzz7MUjp1mvUz3HHHVfYbLPNsnrt2bNn4dJLL82+f4vUa+lp6Ds0Dpo0pd7+85//FA488MBCx44ds8arM888s/rUU5RevTb0fo4lflsVqdfGq4h/mto6DgAAAKyYMd0AAACQE6EbAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QBAg84///y00047rfLjfPrpp2mbbbZJTzzxxCo9znHHHZcGDx6cSsF1112XDjnkkJYuBgAlTugGYI0ya9as9L3vfS99/vOfT+3bt0/du3fPgtMjjzzSqkNtXr7//e83y76JgLrVVlulPffcc5Ue54orrki33HJLak7jxo1LFRUV6aOPPmrS/b71rW+lZ555Jv39739v1vIAUF6EbgDWGP/5z3/Srrvumh599NF08cUXp+effz49+OCDad99902nnHJKKmVLlixpkeddZ5110kYbbbRKj1EoFNJVV12VTjjhhFUuz3rrrZfWX3/9VArWWmutdNRRR6Vf//rXLV0UAEqY0A3AGuO73/1u1qL5z3/+M331q19NX/jCF9IOO+yQhg0bliZNmpTdJlpR4zZ1l2iRDk899VQaOHBg2njjjbMAuPfee2etnTUDZtx2iy22yFrSN9tss3TaaafVW554rhEjRqSpU6dWP0+xFTf+vvbaa9Ohhx6a1l577fSzn/0s7bbbbumSSy6pvn90s27Xrl2aP39+dvmtt97K7vfqq69ml3//+99n91l33XVT165ds4D47rvvLtPCGy3ZcbtOnTplLdHTpk1rsCV+Rdtfn8mTJ6fXXnstHXzwwbUOgMRz33HHHem///u/U8eOHdMXv/jF9O9//zt7jihPBP4DDzwwvffeew12L99nn32y/Xv22WenDTfcMNvOYl3VfJ5nn322el20aMe62P64Pg66hA022CBbH8/xu9/9LjvYsHjx4lrbEs/9zW9+s/py9JK4995706JFi5a7DwBYcwndAKwRPvjgg6xVO1q0I8TWVWw9PfLII9PMmTOrl9tuuy21bds27bXXXtn1H3/8cTr22GPT448/ngX1bbfdNh100EHZ+vDnP/85XX755ek3v/lNeuWVV9Ldd9+ddtxxx3rLFM915plnZsG/+HyxrijC4+GHH561yEdX5gi4ERSL4T66NUe5oyxh/PjxafPNN8/GThdbx0eOHJmF+ihHBMwIlHX9+Mc/Tpdeeml6+umns22N52rIira/PlHOOMAR4b+u8847L51zzjlZcI/njgMDEaCjG3ncLw4g/OQnP0nLc+utt2Z1+uSTT6Zf/vKX6YILLkhjx45NjRHDC6LOQhxsiDqI5z7iiCPS0qVLs0BdFAcs/vrXv9baP3Fw4LPPPsueGwDq07betQBQZiK8RVDdbrvtlnu7aHGNJUTrbIT0n//851nrbthvv/1q3f7666/Pgm8E3v/5n/9JM2bMyFpbBwwYkLVCR4v37rvv3uBzRWtuhM24T10RQI8//vharbo33nhjFgZfeOGFrHtzhPQI4gcccED2fwTzoprhMMawRzfoaE2OlvF43qJoRS/e74c//GHWIv3JJ5+kDh06LFOmFW1/fd54442sxb+hMeP7779/9vfpp5+ehgwZkrW8Fw9yRJf0FY3h7tOnTxbeQxwEiK7s8RjFOlueNm3aZC3kYdNNN63VdT32/80335wF8PCHP/whq8+oh6LoHRAt/rGNAFAfLd0ArBEicDfF3LlzsxAZAfSss86qXj979ux00kknZeEuwlbnzp2zEBthO0RAi67GEXLjdmPGjMlaQldGtKLWFN2wo0V5ypQpWciNoBwBsNj6HetqBsLo1h3dnyMoRitzMVgXy1oztBZ97nOfy/6v2Q29phVtf31if9QX4Os+d5cuXbL/a/YMiHUNlaW+xyhuw4ru0xixnQ8//HB6++23s8sR/qOnQHRBr3vwZOHChav8fACUJ6EbgDVChMQISy+//PIKbxstydGCHIEyWnJriq7VMT44uiDH6a/i7xj7G6fEKnZXjm7K11xzTRbGYhx5//79V2oitLrd4KMVtm/fvlnILgbseOwI4TEWOrqzF4P1ggULshbk2IY//vGP2TjpOAAQimUtihb5omKgrKqqqrdMK9r++sT47w8//LDe6+p77rrrGipLfY9R9z6VlZXLHHRpbF3svPPO2f6O8d1xAOPFF1+st3t+DF3YZJNNGvWYAKx5hG4A1gjRhThC6NVXX50F0rpqni7qjDPOyMZRxzjoui20//jHP7KJu2Icc4zFjsnS3n///Vq3ibAdLczRnTsC8sSJE7PHq090EY+Q31gRqh977LE0YcKELHTHdvXq1SvrIh4tvDF2OsTBhTlz5qSLLrooayGPbvXN0frbmO2vL7xGeZra26A5FMNwjNUuqjmpWrEOQn31cOKJJ2Yt3NHNPIYMxEGVmmIIQnTFj20EgPoI3QCsMSJwR7CKMdYxeVa0DL/00ktZOO7Xr192mwhX0Uod55WOFtM4r3csxRnCo8U8ZgWP+8XkWUcffXT1GPAQAS3GXceY69dffz0bBxzX9+jRo94ybbnllmn69OlZEIzwWne27LoiaD/00EPZOPDi+PRYF63ZNcdzR5fyCJNXXnllVo6YECwmVVtVK9r++sTs4LH/oqV4dYuy7bHHHtnBhyhz9BCIidtqirqJur7vvvuymdKLdV0c1x2zwv/2t7+td4K5mOwthhJsvfXWq2V7AGh9hG4A1hgRjmKW7AiBMWt47969s8m2YtKtOD1XiFAWwTxO1RUtx8WleKquCNTRVXqXXXbJTh0Vrb4xAVfNLuAR0GIisBhr/Le//S395S9/afBc13HqspgELcoUrbIxW/ryRKt1dJ2uGbAjdEeZa47njseKAwCjR49O22+/fRY6a55ubGWtaPvrE9ses7DHgYGWcNNNN2Xj6uMc7UOHDk0//elPa10fM77HqdtiErkYQ37qqadWXxfj1qOOYuK5mqcqK4r6irHfANCQikJL9PUCANYozz33XHaAI7pj15w5vTX48pe/nHWljx4RNUXLfczmHuPpI5wDQH2EbgBgtYiW92htbui85aUmWvRjTP7Xvva19K9//Sv17Nmz1vXRiyF6GBRPeQYA9RG6AQAaGG8fwfvcc8/NzicOACtD6AYAAICcmEgNAAAAciJ0AwAAQE6EbgAAAMiJ0A0AAAA5EboBAAAgJ0I3AAAA5EToBgAAgJwI3QAAAJAToRsAAABSPv4fFUOjdZPLLhoAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Filtruj filmy danego gatunku\n",
    "long_runtime_movies = merged[merged[\"genre_name\"] == longest_runtime_genre]\n",
    "\n",
    "# Histogram czasu trwania\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.hist(long_runtime_movies[\"runtime\"].dropna(), bins=20, color='skyblue', edgecolor='black')\n",
    "plt.title(f\"Histogram czasu trwania filmów - {longest_runtime_genre}\")\n",
    "plt.xlabel(\"Czas trwania (minuty)\")\n",
    "plt.ylabel(\"Liczba filmów\")\n",
    "plt.grid(True)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "481ce544",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
