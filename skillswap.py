CUSTOM_CSS = """
<style>

/* ============================================================
   SKILLSWAP — COMPLETE DARK CAMPUS THEME
   ============================================================ */

/* ---------- FULL APPLICATION ---------- */

html,
body {
    background: #050816 !important;
    color: #F8FAFC !important;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(99, 102, 241, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(168, 85, 247, 0.12),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #050816 0%,
            #080D1D 45%,
            #0B1022 100%
        ) !important;

    color: #F8FAFC !important;
    min-height: 100vh;
}


/* ---------- STREAMLIT MAIN ---------- */

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

.main {
    background: transparent !important;
}

.main .block-container {
    background: transparent !important;
    max-width: 1200px !important;
    padding-top: 35px !important;
    padding-bottom: 60px !important;
}


/* ---------- HEADER ---------- */

[data-testid="stHeader"] {
    background: #050816 !important;
}


/* ============================================================
   TEXT
   ============================================================ */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #FFFFFF !important;
}

p {
    color: #CBD5E1 !important;
}

label {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

span {
    color: inherit;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #030712 0%,
            #080D1D 50%,
            #050816 100%
        ) !important;

    border-right: 1px solid #1E293B !important;
}

[data-testid="stSidebar"] > div {
    background: transparent !important;
}

[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}


/* Sidebar buttons */

[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    color: #CBD5E1 !important;
    border: 1px solid transparent !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(99,102,241,0.15) !important;
    border-color: rgba(129,140,248,0.25) !important;
    color: #FFFFFF !important;
}


/* ============================================================
   SIGNUP / LOGIN FORM
   ============================================================ */

/* Labels */

.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stNumberInput label {
    color: #FFFFFF !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}


/* Input containers */

.stTextInput > div > div,
.stTextArea > div > div,
.stNumberInput > div > div {

    background: #10182B !important;

    border-radius: 12px !important;
}


/* Actual input */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {

    background: #10182B !important;

    color: #FFFFFF !important;

    caret-color: #A5B4FC !important;

    border: 1px solid #334155 !important;

    border-radius: 12px !important;

    padding: 12px 14px !important;

    font-size: 15px !important;
}


/* Input hover */

.stTextInput input:hover,
.stTextArea textarea:hover,
.stNumberInput input:hover {

    border-color: #475569 !important;
}


/* Input focus */

.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus {

    background: #111C33 !important;

    color: #FFFFFF !important;

    border: 2px solid #818CF8 !important;

    box-shadow:
        0 0 0 3px rgba(99,102,241,0.15) !important;
}


/* Placeholder */

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {

    color: #94A3B8 !important;

    opacity: 1 !important;
}


/* Password */

input[type="password"] {

    color: #FFFFFF !important;

    background: #10182B !important;
}


/* ============================================================
   SELECT BOX
   ============================================================ */

[data-baseweb="select"] > div {

    background: #10182B !important;

    color: #FFFFFF !important;

    border: 1px solid #334155 !important;

    border-radius: 12px !important;

    min-height: 42px;
}

[data-baseweb="select"] span {

    color: #FFFFFF !important;
}


/* Dropdown */

[data-baseweb="popover"] {

    background: #0B1120 !important;

    border: 1px solid #26324D !important;
}

[data-baseweb="menu"] {

    background: #0B1120 !important;
}

[role="option"] {

    background: #0B1120 !important;

    color: #E2E8F0 !important;
}

[role="option"]:hover {

    background: #312E81 !important;

    color: #FFFFFF !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {

    background:
        linear-gradient(
            135deg,
            #6366F1,
            #8B5CF6
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 12px !important;

    font-weight: 700 !important;

    min-height: 42px;

    padding: 8px 20px !important;

    box-shadow:
        0 8px 20px rgba(99,102,241,0.25) !important;
}

.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #4F46E5,
            #7C3AED
        ) !important;

    color: #FFFFFF !important;

    transform: translateY(-1px);

    box-shadow:
        0 12px 28px rgba(99,102,241,0.35) !important;
}


/* ============================================================
   CARDS
   ============================================================ */

.ss-card {

    background:
        linear-gradient(
            145deg,
            #111A30,
            #0B1224
        ) !important;

    border: 1px solid #26324D !important;

    border-radius: 18px !important;

    padding: 24px !important;

    margin-bottom: 18px;

    color: #F8FAFC !important;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.25) !important;
}

.ss-card:hover {

    border-color: #4F46E5 !important;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.35) !important;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

.ss-metric {

    background:
        linear-gradient(
            145deg,
            #111A30,
            #0B1224
        ) !important;

    border: 1px solid #26324D !important;

    border-radius: 18px !important;

    padding: 22px !important;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.25) !important;
}

.ss-metric h2 {

    color: #A5B4FC !important;

    font-size: 30px !important;

    font-weight: 800 !important;
}

.ss-metric p {

    color: #94A3B8 !important;
}


/* ============================================================
   HERO
   ============================================================ */

.ss-hero {

    background:
        radial-gradient(
            circle at 90% 20%,
            rgba(236,72,153,0.25),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #312E81,
            #581C87,
            #111827
        ) !important;

    border: 1px solid rgba(167,139,250,0.25) !important;

    border-radius: 22px !important;

    padding: 32px !important;

    margin-bottom: 25px;

    box-shadow:
        0 20px 45px rgba(0,0,0,0.35) !important;
}

.ss-hero h1,
.ss-hero h2,
.ss-hero h3,
.ss-hero p {

    color: #FFFFFF !important;
}


/* ============================================================
   BADGES
   ============================================================ */

.ss-badge {

    display: inline-block;

    padding: 6px 12px;

    border-radius: 999px;

    background: rgba(99,102,241,0.16);

    border: 1px solid rgba(129,140,248,0.30);

    color: #A5B4FC !important;

    font-size: 13px;

    font-weight: 700;
}


/* ============================================================
   TABS
   ============================================================ */

button[data-baseweb="tab"] {

    background: transparent !important;

    color: #64748B !important;

    font-weight: 600 !important;
}

button[data-baseweb="tab"]:hover {

    color: #CBD5E1 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {

    color: #A5B4FC !important;
}


/* ============================================================
   ALERTS
   ============================================================ */

.stAlert {

    background: #10182B !important;

    color: #F8FAFC !important;

    border: 1px solid #26324D !important;

    border-radius: 14px !important;
}


/* ============================================================
   EXPANDERS
   ============================================================ */

[data-testid="stExpander"] {

    background: #0D1427 !important;

    border: 1px solid #26324D !important;

    border-radius: 14px !important;
}

[data-testid="stExpander"] * {

    color: #E2E8F0 !important;
}


/* ============================================================
   CHECKBOX
   ============================================================ */

[data-testid="stCheckbox"] label {

    color: #CBD5E1 !important;
}


/* ============================================================
   RADIO
   ============================================================ */

[data-testid="stRadio"] label {

    color: #CBD5E1 !important;
}


/* ============================================================
   FILE UPLOADER
   ============================================================ */

[data-testid="stFileUploader"] {

    background: #0D1427 !important;

    border: 1px dashed #475569 !important;

    border-radius: 14px !important;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {

    background: #0D1427 !important;

    border: 1px solid #26324D !important;

    border-radius: 14px !important;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {

    border-color: #26324D !important;
}


/* ============================================================
   SMALL TEXT
   ============================================================ */

small {

    color: #94A3B8 !important;
}


/* ============================================================
   LINKS
   ============================================================ */

a {

    color: #A5B4FC !important;

    text-decoration: none !important;
}

a:hover {

    color: #C4B5FD !important;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-track {

    background: #050816;
}

::-webkit-scrollbar-thumb {

    background: #334155;

    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {

    background: #6366F1;
}


/* ============================================================
   FOOTER
   ============================================================ */

footer {

    background: #050816 !important;

    color: #64748B !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .main .block-container {

        padding: 18px !important;
    }

    .ss-card {

        padding: 18px !important;
    }

    .ss-hero {

        padding: 22px !important;

        border-radius: 18px !important;
    }

    h1 {

        font-size: 28px !important;
    }
}

</style>
"""