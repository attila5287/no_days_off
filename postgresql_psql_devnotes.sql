-- psql
CREATE TABLE post (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id BIGINT NOT NULL REFERENCES public.user 
)

-- sql
CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	date_posted DATETIME NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
)
-- psql
CREATE TABLE "proday" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"title"	VARCHAR(100),
	"desc"	VARCHAR(100),
	"date_posted"	TIMESTAMP,
	"cat01"	VARCHAR(100),
	"act01"	VARCHAR(100),
	"done01"	BOOLEAN,
	"cat02"	VARCHAR(100),
	"act02"	VARCHAR(100),
	"done02"	BOOLEAN,
	"act03"	VARCHAR(100),
	"cat03"	VARCHAR(100),
	"done03"	BOOLEAN,
	"cat04"	VARCHAR(100),
	"act04"	VARCHAR(100),
	"done04"	BOOLEAN,
	"icon01"	VARCHAR(100),
	"icon02"	VARCHAR(100),
	"icon03"	VARCHAR(100),
	"icon04"	VARCHAR(100),
	"count_c01"	SMALLINT,
	"count_c02"	SMALLINT,
	"count_c03"	SMALLINT,
	"count_c04"	SMALLINT,
	"countD_c01"	SMALLINT,
	"countD_c02"	SMALLINT,
	"countD_c03"	SMALLINT,
	"countD_c04"	SMALLINT,
	"count_done"	SMALLINT,
	"count_total"	SMALLINT,
	"perc_done"	SMALLINT,
	"message_total"	VARCHAR(256),
    "user_id"	BIGINT REFERENCES public.user
)

-- SQLITE
CREATE TABLE "proday" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"title"	VARCHAR(100),
	"desc"	VARCHAR(100),
	"date_posted"	DATETIME,
	"user_id"	VARCHAR(100),
	"cat01"	VARCHAR(100),
	"act01"	VARCHAR(100),
	"done01"	REAL,
	"cat02"	VARCHAR(100),
	"act02"	VARCHAR(100),
	"done02"	REAL,
	"act03"	VARCHAR(100),
	"cat03"	VARCHAR(100),
	"done03"	REAL,
	"cat04"	VARCHAR(100),
	"act04"	VARCHAR(100),
	"done04"	REAL,
	"icon01"	VARCHAR(100),
	"icon02"	VARCHAR(100),
	"icon03"	VARCHAR(100),
	"icon04"	VARCHAR(100),
	"count_c01"	INTEGER,
	"count_c02"	INTEGER,
	"count_c03"	INTEGER,
	"count_c04"	INTEGER,
	"countD_c01"	INTEGER,
	"countD_c02"	INTEGER,
	"countD_c03"	INTEGER,
	"countD_c04"	INTEGER,
	"count_done"	INTEGER,
	"count_total"	INTEGER,
	"perc_done"	INTEGER,
	"message_total"	VARCHAR(256)
)

-- postgres
CREATE TABLE "task" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"title"	VARCHAR(32) NOT NULL,
	"content"	TEXT,
	"done"	BOOLEAN,
	"is_urgent"	TEXT,
	"is_important"	TEXT,
	"matrix_zone"	TEXT,
	"border_style"	TEXT,
	"urg_points"	SMALLINT,
	"imp_points"	SMALLINT,
	"date_posted"	TIMESTAMP,
	"user_id"	BIGINT REFERENCES public.user
)
-- sqlite
CREATE TABLE "task" (
	"id"	INTEGER NOT NULL,
	"title"	INTEGER,
	"content"	NUMERIC,
	"done"	REAL,
	"is_urgent"	TEXT,
	"is_important"	TEXT,
	"matrix_zone"	TEXT,
	"border_style"	TEXT,
	"urg_points"	INTEGER,
	"imp_points"	INTEGER,
	"date_posted"	DATETIME,
	"user_id"	INTEGER,
	PRIMARY KEY("id")
)

-- postgresql edt, need to run first in psql shell
CREATE TABLE "user" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"username"	VARCHAR(20) NOT NULL UNIQUE,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"image_file"	VARCHAR(32) NOT NULL,
	"password"	VARCHAR(60) NOT NULL,
	"imp_pts"	INTEGER,
	"urg_pts"	INTEGER,
	"total_pts"	INTEGER,
	"imp_perc"	INTEGER,
	"urg_perc"	INTEGER,
	"avatar_img"	TEXT,
	"avatar_mode"	TEXT
)
-- SQLITE
CREATE TABLE "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(20) NOT NULL UNIQUE,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"image_file"	VARCHAR(20) NOT NULL,
	"password"	VARCHAR(60) NOT NULL,
	"imp_pts"	INTEGER,
	"urg_pts"	INTEGER,
	"total_pts"	INTEGER,
	"imp_perc"	INTEGER,
	"urg_perc"	INTEGER,
	"avatar_img"	BLOB,
	"avatar_mode"	TEXT,
	PRIMARY KEY("id")
)

-- psql command that actually works
CREATE TABLE post (
	id INTEGER NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL REFERENCES user, 
)

-- sqlite browser copy create statement
CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	date_posted DATETIME NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
)



-- postgresql-flat-26247=#
--  DROP TABLE public.user;

-- postgresql-flat-26247
-- ================================
-- The format of a psql command is the backslash, followed immediately by a command verb, then any
-- arguments. The arguments are separated from the command verb and each other by any number of
-- whitespace characters.

-- Plan:                  Hobby-dev
-- Status:                Available
-- Connections:           0/20
-- PG Version:            11.6
-- Created:               2019-12-28 01:38 UTC
-- Data Size:             7.8 MB
-- Tables:                4
-- Rows:                  0/10000 (In compliance)
-- Fork/Follow:           Unsupported
-- Rollback:              Unsupported
-- Continuous Protection: Off
-- Add-on:                postgresql-flat-26247

--             List of relations
--  Schema |  Name  | Type  |     Owner
-- --------+--------+-------+----------------
--  public | post   | table | itdjzuakoxytrq
--  public | proday | table | itdjzuakoxytrq
--  public | task   | table | itdjzuakoxytrq
--  public | user   | table | itdjzuakoxytrq
-- (4 rows)


-- nodaysoff::DATABASE-> DROP TABLE public.post
-- nodaysoff::DATABASE-> ;
-- ERROR:  syntax error at or near "=#"
-- LINE 1: =#
--         ^
-- nodaysoff::DATABASE=>
-- nodaysoff::DATABASE=> =# \rt
-- invalid command \rt
-- Try \? for help.
-- nodaysoff::DATABASE-> =# \d?
-- invalid command \d?
-- Try \? for help.
-- nodaysoff::DATABASE-> =# \?
-- The system cannot find the path specified.
-- General
--   \copyright             show PostgreSQL usage and distribution terms
--   \crosstabview [COLUMNS] execute query and display results in crosstab
--   \errverbose            show most recent error message at maximum verbosity
--   \g [FILE] or ;         execute query (and send results to file or |pipe)
--   \gdesc                 describe result of query, without executing it
--   \gexec                 execute query, then execute each value in its result
--   \gset [PREFIX]         execute query and store results in psql variables
--   \gx [FILE]             as \g, but forces expanded output mode
--   \q                     quit psql
--   \watch [SEC]           execute query every SEC seconds

-- Help
--   \? [commands]          show help on backslash commands
--   \? options             show help on psql command-line options
--   \? variables           show help on special variables
--   \h [NAME]              help on syntax of SQL commands, * for all commands

-- Query Buffer
--   \e [FILE] [LINE]       edit the query buffer (or file) with external editor
--   \ef [FUNCNAME [LINE]]  edit function definition with external editor
--   \ev [VIEWNAME [LINE]]  edit view definition with external editor
--   \p                     show the contents of the query buffer
--   \r                     reset (clear) the query buffer
--   \w FILE                write query buffer to file

-- Input/Output
--   \copy ...              perform SQL COPY with data stream to the client host
--   \echo [STRING]         write string to standard output
--   \i FILE                execute commands from file
--   \ir FILE               as \i, but relative to location of current script
--   \o [FILE]              send all query results to file or |pipe
--   \qecho [STRING]        write string to query output stream (see \o)

-- Conditional
--   \if EXPR               begin conditional block
--   \elif EXPR             alternative within current conditional block
--   \else                  final alternative within current conditional block
--   \endif                 end conditional block

-- Informational
--   (options: S = show system objects, + = additional detail)
--   \d[S+]                 list tables, views, and sequences
--   \d[S+]  NAME           describe table, view, sequence, or index
--   \da[S]  [PATTERN]      list aggregates
--   \dA[+]  [PATTERN]      list access methods
--   \db[+]  [PATTERN]      list tablespaces
--   \dc[S+] [PATTERN]      list conversions
--   \dC[+]  [PATTERN]      list casts
--   \dd[S]  [PATTERN]      show object descriptions not displayed elsewhere
--   \dD[S+] [PATTERN]      list domains
--   \ddp    [PATTERN]      list default privileges
--   \dE[S+] [PATTERN]      list foreign tables
--   \det[+] [PATTERN]      list foreign tables
--   \des[+] [PATTERN]      list foreign servers
--   \deu[+] [PATTERN]      list user mappings
--   \dew[+] [PATTERN]      list foreign-data wrappers
--   \df[anptw][S+] [PATRN] list [only agg/normal/procedures/trigger/window] functions
--   \dF[+]  [PATTERN]      list text search configurations
--   \dFd[+] [PATTERN]      list text search dictionaries
--   \dFp[+] [PATTERN]      list text search parsers
--   \dFt[+] [PATTERN]      list text search templates
--   \dg[S+] [PATTERN]      list roles
--   \di[S+] [PATTERN]      list indexes
--   \dl                    list large objects, same as \lo_list
--   \dL[S+] [PATTERN]      list procedural languages
--   \dm[S+] [PATTERN]      list materialized views
--   \dn[S+] [PATTERN]      list schemas
--   \do[S]  [PATTERN]      list operators
--   \dO[S+] [PATTERN]      list collations
--   \dp     [PATTERN]      list table, view, and sequence access privileges
--   \dP[itn+] [PATTERN]    list [only index/table] partitioned relations [n=nested]
--   \drds [PATRN1 [PATRN2]] list per-database role settings
--   \dRp[+] [PATTERN]      list replication publications
--   \dRs[+] [PATTERN]      list replication subscriptions
--   \ds[S+] [PATTERN]      list sequences
--   \dt[S+] [PATTERN]      list tables
--   \dT[S+] [PATTERN]      list data types
--   \du[S+] [PATTERN]      list roles
--   \dv[S+] [PATTERN]      list views
--   \dx[+]  [PATTERN]      list extensions
--   \dy     [PATTERN]      list event triggers
--   \l[+]   [PATTERN]      list databases
--   \sf[+]  FUNCNAME       show a function's definition
--   \sv[+]  VIEWNAME       show a view's definition
--   \z      [PATTERN]      same as \dp

-- Formatting
--   \a                     toggle between unaligned and aligned output mode
--   \C [STRING]            set table title, or unset if none
--   \f [STRING]            show or set field separator for unaligned query output
--   \H                     toggle HTML output mode (currently off)
--   \pset [NAME [VALUE]]   set table output option
--                          (border|columns|csv_fieldsep|expanded|fieldsep|
--                          fieldsep_zero|footer|format|linestyle|null|
--                          numericlocale|pager|pager_min_lines|recordsep|
--                          recordsep_zero|tableattr|title|tuples_only|
--                          unicode_border_linestyle|unicode_column_linestyle|
--                          unicode_header_linestyle)
--   \t [on|off]            show only rows (currently off)
--   \T [STRING]            set HTML <table> tag attributes, or unset if none
--   \x [on|off|auto]       toggle expanded output (currently off)

-- Connection
--   \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
--                          connect to new database (currently "dcrjqdnonkc3m0")
--   \conninfo              display information about current connection
--   \encoding [ENCODING]   show or set client encoding
--   \password [USERNAME]   securely change the password for a user

-- Operating System
--   \cd [DIR]              change the current working directory
--   \setenv NAME [VALUE]   set or unset environment variable
--   \timing [on|off]       toggle timing of commands (currently off)
--   \! [COMMAND]           execute command in shell or start interactive shell

-- Variables
--   \prompt [TEXT] NAME    prompt user to set internal variable
--   \set [NAME [VALUE]]    set internal variable, or list all if no parameters
--   \unset NAME            unset (delete) internal variable

-- Large Objects
--   \lo_export LOBOID FILE
--   \lo_import FILE [COMMENT]
--   \lo_list
--   \lo_unlink LOBOID      large object operations