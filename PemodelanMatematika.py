import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="EOQ Calculator",
    page_icon="📦",
    layout="centered"
)

# Judul utama
st.title("📦 EOQ (Economic Order Quantity) Calculator")
st.markdown("Hitung jumlah pemesanan optimal untuk meminimalkan biaya persediaan.")

st.divider()

# Sidebar input
st.sidebar.header("📥 Input Data")
D = st.sidebar.number_input("Permintaan tahunan (unit)", min_value=1, value=100000)
S = st.sidebar.number_input("Biaya pemesanan per order (Rp)", min_value=1, value=2000000)
H = st.sidebar.number_input("Biaya penyimpanan per unit per tahun (Rp)", min_value=1, value=5000)

# Hitung EOQ
EOQ = np.sqrt((2 * D * S) / H)
orders_per_year = D / EOQ
total_order_cost = orders_per_year * S
average_inventory = EOQ / 2
total_holding_cost = average_inventory * H
total_inventory_cost = total_order_cost + total_holding_cost

# Output hasil
st.subheader("📊 Hasil Perhitungan")
col1, col2 = st.columns(2)

with col1:
    st.metric("EOQ", f"{EOQ:.0f} unit")
    st.metric("Jumlah Pemesanan/Tahun", f"{orders_per_year:.2f} kali")
with col2:
    st.metric("Total Biaya Pemesanan", f"Rp {total_order_cost:,.0f}")
    st.metric("Total Biaya Penyimpanan", f"Rp {total_holding_cost:,.0f}")

st.success(f"💡 **Total Biaya Persediaan: Rp {total_inventory_cost:,.0f} / tahun**")

# Grafik visualisasi
st.subheader("📈 Grafik Biaya Persediaan")
order_range = np.arange(1000, D, 100)
total_costs = ((D / order_range) * S) + ((order_range / 2) * H)

fig, ax = plt.subplots()
ax.plot(order_range, total_costs, label="Total Biaya Persediaan", color='royalblue')
ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ ≈ {EOQ:.0f} unit')
ax.set_xlabel("Jumlah Pemesanan per Order")
ax.set_ylabel("Total Biaya (Rp)")
ax.set_title("Kurva Total Biaya vs Jumlah Pemesanan")
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("© 2025 - EOQ Simulator by Fullstack Engineer | Powered by Streamlit")

