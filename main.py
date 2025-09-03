# -*- coding: utf-8 -*-
# pip install streamlit

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
# โหลดไฟล์
file_path = "Supervised Learning Project.xlsx"
df = pd.read_excel(file_path, sheet_name="การตอบแบบฟอร์ม 1")

# ลบช่องว่างในชื่อคอลัมน์
df.columns = df.columns.str.strip()

# เลือก features และ target
X = df[[
        '1. คุณสนใจทำงานด้านใดในสายงาน IT มากที่สุด?',
        '2. คุณถนัดการเขียนโปรแกรมด้วยภาษาใดมากที่สุด?',
        '3. คุณมีความสนใจในการทำงานเป็นทีมมากน้อยเพียงใด?',
        '4. เมื่อเกิดปัญหาทางเทคนิค คุณมักจะทำอย่างไร?',
        '6. คุณเคยมีประสบการณ์การทำโปรเจกต์ IT แบบใดบ้าง?']]

y = df['ปัจจุบันคุณทำงานอาชีพอะไรในสายงาน IT?']

# เข้ารหัส categorical data
le_dict = {}
for col in X.columns:
    if X[col].dtype == 'object':
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        le_dict[col] = le

# เข้ารหัส target
le_target = LabelEncoder()
y = le_target.fit_transform(y.astype(str))

# แบ่ง train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scale ข้อมูลให้เหมาะกับ Neural Network
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# สร้างโมเดล MLP (Neural Network) เทรน 1000 epochs
model = MLPClassifier(hidden_layer_sizes=(64, 32),
                      max_iter=1000,   # จำนวน epochs = 1000
                      activation='relu',
                      solver='adam',
                      random_state=42)

# เทรนโมเดล
model.fit(X_train, y_train)

# ทำนายผล
y_pred = model.predict(X_test)

# ประเมินผล
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=le_target.classes_))


st.set_page_config(page_title="PredictIQ ", page_icon="📊", layout="centered")
# แทนที่ st.title("🧠 PredictIQ 🧠") ด้วยบล็อกนี้
st.markdown(
    """
    <style>
      .center-title{
        text-align:center; font-weight:800; font-size:2rem; line-height:1.2;
      }
      .tagline{
        text-align:center; font-size:1.05rem; opacity:.85; margin-top:4px;
      }
    </style>
    <div class="center-title">🧠 PredictIQ 🧠</div>
    <div class="tagline">อนาคตขึ้นอยู่กับมือคุณ · <i>The future is in your hands.</i></div>
    """,
    unsafe_allow_html=True
)



# ---------------------------
# ช้อยส์เหมือนแบบฟอร์ม (ข้อ 1–7)
# ---------------------------

# เพศ
gender_opts = ["ชาย", "หญิง", "อื่น ๆ"]

# 1) สนใจทำงานด้านใดในสายงาน IT มากที่สุด?
q1_opts = [
    "ก. การพัฒนาเว็บไซต์หรือแอปพลิเคชัน",
    "ข. การดูแลระบบเครือข่ายและความปลอดภัย",
    "ค. การวิเคราะห์ข้อมูลและวิทยาการข้อมูล (Data Science)",
    "ง. การทดสอบระบบและควบคุมคุณภาพ (QA)",
    "จ. ไม่แน่ใจ / ยังไม่ทราบ",
]

# 2) ถนัดภาษาใดมากที่สุด?
q2_opts = ["ก. Python", "ข. Java", "ค. JavaScript", "ง. C/C++", "จ. ยังไม่มีความถนัด / ไม่เคยเขียนโปรแกรม"]

# 3) สนใจทำงานเป็นทีมมากน้อยเพียงใด?
q3_opts = ["ก. มากที่สุด", "ข. มาก", "ค. ปานกลาง", "ง. น้อย", "จ. ไม่ชอบทำงานเป็นทีมเลย"]

# 4) เมื่อเกิดปัญหาทางเทคนิค มักทำอย่างไร?
q4_opts = [
    "ก. พยายามค้นหาข้อมูลแก้ไขด้วยตนเองก่อน",
    "ข. ปรึกษาเพื่อนร่วมงานหรือคนที่มีประสบการณ์",
    "ค. แจ้งหัวหน้าหรือผู้ดูแลระบบทันที",
    "ง. รอให้ผู้อื่นมาแก้ให้",
    "จ. หลีกเลี่ยงการทำงานที่เกี่ยวกับเทคนิค",
]

# 5) ถนัดด้านใดมากที่สุด?
q5_opts = [
    "ก. การวิเคราะห์และแก้ปัญหา",
    "ข. การออกแบบและสร้างระบบ",
    "ค. การสื่อสารและประสานงาน",
    "ง. การจัดการข้อมูลและฐานข้อมูล",
    "จ. การเขียนโค้ดและทดสอบระบบ",
]

# 6) เคยมีประสบการณ์โปรเจกต์ IT แบบใดบ้าง?
q6_opts = [
    "ก. พัฒนาเว็บไซต์หรือแอป",
    "ข. วิเคราะห์ข้อมูล/สร้าง Dashboard",
    "ค. เขียน Script หรือ Automate ระบบ",
    "ง. ทดสอบระบบหรือดูแลคุณภาพซอฟต์แวร์",
    "จ. ยังไม่เคยทำโปรเจกต์ IT",
]

# 7) อาชีพในสาย IT (ถ้ามี)?
q7_opts = [
    "ก. นักพัฒนาเว็บไซต์/แอปพลิเคชัน (Web/Mobile Developer)",
    "ข. ผู้ดูแลระบบเครือข่ายและความปลอดภัย (Network & Security Admin)",
    "ค. นักวิเคราะห์ข้อมูล/นักวิทยาศาสตร์ข้อมูล (Data Analyst / Data Scientist)",
    "ง. ผู้ทดสอบระบบและควบคุมคุณภาพ (QA/Test Engineer)",
]

# ---------------------------
# Rule-based predictor (เดโม)
# ---------------------------
CATS = [
    "Software Development",
    "Network/Security",
    "Data Science / Analytics",
    "Quality Assurance (QA)",
    "General / Undecided",
]

def predict_score(sel1, sel2, sel3, sel4, sel5, sel6, sel7):
    sc = {c: 0 for c in CATS}

    # Q1: ความสนใจหลัก
    if sel1.startswith("ก."): sc["Software Development"] += 35
    if sel1.startswith("ข."): sc["Network/Security"] += 35
    if sel1.startswith("ค."): sc["Data Science / Analytics"] += 35
    if sel1.startswith("ง."): sc["Quality Assurance (QA)"] += 35
    if sel1.startswith("จ."): sc["General / Undecided"] += 25

    # Q2: ภาษาโปรแกรม
    if sel2.startswith("ก."): sc["Data Science / Analytics"] += 12; sc["Software Development"] += 6
    if sel2.startswith("ข."): sc["Software Development"] += 10
    if sel2.startswith("ค."): sc["Software Development"] += 12
    if sel2.startswith("ง."): sc["Software Development"] += 8
    if sel2.startswith("จ."): sc["General / Undecided"] += 8

    # Q3: การทำงานเป็นทีม
    if sel3.startswith(("ก.","ข.")): sc["Quality Assurance (QA)"] += 8
    elif sel3.startswith("ค."): sc["Software Development"] += 4
    elif sel3.startswith(("ง.","จ.")): sc["General / Undecided"] += 5

    # Q4: วิธีแก้ปัญหา
    if sel4.startswith("ก."): sc["Data Science / Analytics"] += 8; sc["Software Development"] += 6
    if sel4.startswith("ข."): sc["Quality Assurance (QA)"] += 6
    if sel4.startswith("ค."): sc["Network/Security"] += 6
    if sel4.startswith("ง."): sc["General / Undecided"] += 4
    if sel4.startswith("จ."): sc["General / Undecided"] += 8

    # Q5: ความถนัด
    if sel5.startswith("ก."): sc["Data Science / Analytics"] += 12
    if sel5.startswith("ข."): sc["Software Development"] += 12
    if sel5.startswith("ค."): sc["Quality Assurance (QA)"] += 10
    if sel5.startswith("ง."): sc["Data Science / Analytics"] += 10
    if sel5.startswith("จ."): sc["Software Development"] += 12

    # Q6: ประสบการณ์โปรเจกต์
    if sel6.startswith("ก."): sc["Software Development"] += 10
    if sel6.startswith("ข."): sc["Data Science / Analytics"] += 10
    if sel6.startswith("ค."): sc["Network/Security"] += 8
    if sel6.startswith("ง."): sc["Quality Assurance (QA)"] += 10
    if sel6.startswith("จ."): sc["General / Undecided"] += 6

    # Q7: อาชีพปัจจุบัน (ถ้ามี)
    if sel7.startswith("ก."): sc["Software Development"] += 6
    if sel7.startswith("ข."): sc["Network/Security"] += 6
    if sel7.startswith("ค."): sc["Data Science / Analytics"] += 6
    if sel7.startswith("ง."): sc["Quality Assurance (QA)"] += 6

    for k in sc: sc[k] = min(100, sc[k])
    best_cat, best_score = max(sc.items(), key=lambda x: x[1])
    top3 = sorted(sc.items(), key=lambda x: x[1], reverse=True)[:3]
    top3_str = ", ".join([f"{k} ({v}%)" for k, v in top3])
    return best_cat, best_score, sc, top3_str

# ---------------------------
# ฟอร์มกรอก (ข้อ 1–7 default เป็น "-")
# ---------------------------
with st.form("it_form"):
    name = st.text_input("ชื่อ *")
    age  = st.number_input("อายุ *", min_value=0, max_value=120, value=20, step=1)
    gender = st.selectbox("เพศ *", ["ชาย", "หญิง", "อื่น ๆ"], index=0)

    st.subheader("You can choose your future.")
    sel1 = st.selectbox("1) คุณสนใจทำงานด้านใดในสายงาน IT มากที่สุด? *", ["-"] + q1_opts, index=0)
    sel2 = st.selectbox("2) คุณถนัดการเขียนโปรแกรมด้วยภาษาใดมากที่สุด? *", ["-"] + q2_opts, index=0)
    sel3 = st.selectbox("3) คุณมีความสนใจในการทำงานเป็นทีมมากน้อยเพียงใด? *", ["-"] + q3_opts, index=0)
    sel4 = st.selectbox("4) เมื่อเกิดปัญหาทางเทคนิค คุณมักจะทำอย่างไร? *", ["-"] + q4_opts, index=0)
    sel5 = st.selectbox("5) คุณคิดว่าตัวเองมีความถนัดด้านใดมากที่สุด? *", ["-"] + q5_opts, index=0)
    sel6 = st.selectbox("6) คุณเคยมีประสบการณ์การทำโปรเจกต์ IT แบบใดบ้าง? *", ["-"] + q6_opts, index=0)
    sel7 = st.selectbox("7) ปัจจุบันคุณทำงานอาชีพอะไรในสายงาน IT? (ถ้ามี) *", ["-"] + q7_opts, index=0)

    submitted = st.form_submit_button("👉Predict👈")

if submitted:
    # ตรวจว่ามีข้อไหนยังเป็น "-" อยู่
    pending = [i for i, s in enumerate([sel1,sel2,sel3,sel4,sel5,sel6,sel7], start=1) if s == "-"]
    if not name or age is None:
        st.warning("กรุณากรอก 'ชื่อ' และ 'อายุ' ให้ครบ")
    elif pending:
        st.warning(f"กรุณาเลือกคำตอบให้ครบทุกข้อ (ยังไม่ได้เลือก: {', '.join(map(str, pending))})")
    else:
        best_cat, best_score, all_scores, top3 = predict_score(sel1, sel2, sel3, sel4, sel5, sel6, sel7)
        
        feature_cols = [
            '1. คุณสนใจทำงานด้านใดในสายงาน IT มากที่สุด?',
        '2. คุณถนัดการเขียนโปรแกรมด้วยภาษาใดมากที่สุด?',
        '3. คุณมีความสนใจในการทำงานเป็นทีมมากน้อยเพียงใด?',
        '4. เมื่อเกิดปัญหาทางเทคนิค คุณมักจะทำอย่างไร?',
        '6. คุณเคยมีประสบการณ์การทำโปรเจกต์ IT แบบใดบ้าง?'
             ]
        tan = pd.DataFrame([[
        sel1, sel2, sel3, sel4, sel6
        ]], columns=feature_cols)

        tan = tan[[
        '1. คุณสนใจทำงานด้านใดในสายงาน IT มากที่สุด?',
        '2. คุณถนัดการเขียนโปรแกรมด้วยภาษาใดมากที่สุด?',
        '3. คุณมีความสนใจในการทำงานเป็นทีมมากน้อยเพียงใด?',
        '4. เมื่อเกิดปัญหาทางเทคนิค คุณมักจะทำอย่างไร?',
        '6. คุณเคยมีประสบการณ์การทำโปรเจกต์ IT แบบใดบ้าง?']]
    
        le_dict = {}
        for col in tan.columns:
            if tan[col].dtype == 'object':
                le = LabelEncoder()
                tan[col] = le.fit_transform(tan[col].astype(str))
                le_dict[col] = le
        train = model.predict(tan)

        if train == 0:
            st.success("Web/Mobile Developer")
        elif train ==1:
            st.success("Network & Security Admin")
        elif train ==2:
            st.success("Data Scientist")
        elif train ==3:
            st.success("QA/Test Engineer")
        
        st.write(
            {
                "ชื่อ": name,
                "อายุ": age,
                "เพศ": gender,
                "แนะนำสายงาน": best_cat,
                "คะแนน(%)": best_score,
                "Top3": top3,
            }
        )
        st.progress(best_score / 100.0)
