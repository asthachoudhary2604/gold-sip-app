import streamlit as st

st.title("🪙 Goal-Based Gold SIP")

target_grams = st.number_input("Target Gold (grams)", value=5.0)
frequency = st.selectbox("SIP Frequency", ["Daily", "Weekly", "Monthly"])
sip_amount = st.number_input(f"{frequency} SIP Amount (₹)", value=3000.0)
months = st.slider("Duration (months)", 1, 12, 5)

prices = [15000, 15200, 14800, 15500, 16000, 15800, 16200, 15900, 16100, 16300, 16500, 16700]

# Convert duration into number of investments
if frequency == "Daily":
    total_investments = months * 30
elif frequency == "Weekly":
    total_investments = months * 4
else:
    total_investments = months

total_grams = 0

for i in range(int(total_investments)):
    grams_bought = sip_amount / prices[i % len(prices)]
    total_grams += grams_bought

progress = min((total_grams / target_grams) * 100, 100)
remaining = max(target_grams - total_grams, 0)

st.subheader("Gold Progress")

# GOLD BAR VISUAL
st.markdown(f"""
<div style="
    width:300px;
    height:60px;
    border:2px solid gold;
    border-radius:10px;
    overflow:hidden;
">
    <div style="
        width:{progress}%;
        height:100%;
        background:linear-gradient(to right,#D4AF37,#FFD700);
    ">
    </div>
</div>
""", unsafe_allow_html=True)

st.write(f"Progress: {round(progress,2)}%")
st.write(f"Accumulated: {round(total_grams,4)} g")
st.write(f"Remaining: {round(remaining,4)} g")

if progress >= 50:
    st.success("On Track ✅")
else:
    st.warning("Behind ⚠️")
