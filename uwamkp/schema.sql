DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS listing;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS reply;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  username TEXT UNIQUE NOT NULL,
  salt TEXT NOT NULL,
  password TEXT NOT NULL,
  created_at TEXT NOT NULL,
--   0 means not admin, 1 means admin
  is_admin INTEGER NOT NULL,
--   0 means not deleted, 1 means deleted
  deleted INTEGER NOT NULL
);


CREATE TABLE listing (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
--   TODO check facebook, define different integers for different condition
  condition INTEGER NOT NULL,
  price REAL NOT NULL,
  description TEXT NOT NULL,
  image BLOB,
  seller_id INTEGER NOT NULL,
-- 0 means not suspended, 1 means suspended
  suspended INTEGER NOT NULL,
-- 0 means not sold, 1 means sold
  sold INTEGER NOT NULL,
-- 0 means not deleted, 1 means deleted
  deleted INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT,
  category_id INTEGER,
  FOREIGN KEY (seller_id) REFERENCES user (id),
  FOREIGN KEY (category_id) REFERENCES category (id)
);


CREATE TABLE reply (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  message TEXT NOT NULL,
  from_user_id INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  listing_id INTEGER NOT NULL,
  FOREIGN KEY (from_user_id) REFERENCES user (id),
  FOREIGN KEY (listing_id) REFERENCES listing (id)
);


--   this will be used in furture
CREATE TABLE category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category_name TEXT UNIQUE NOT NULL,
  desc TEXT,
  created_at TEXT NOT NULL
);
