
import streamlit as st
import calculos as cl

st.title("Kiosco Carlos Paz")

productos = ["Alfajores", "Gaseosas", "Chicles", "Agua"]

cliente = st.text_input ("ingrese su nombre para continuar")
precios = [1500, 2800, 500, 1800]
if cliente != "":
    producto = st.selectbox("Producto", productos)

pos = cl.buscar_posicion(productos, producto)
precio = precios[pos]

fecha = st.date_input("Fecha")

numero = st.number_input("N° de presupuesto", min_value=1, step=1) 

st.write(f"precio por {producto} = {precios[pos]}")

st.write("obtienes un descuento del 10% al pagar en efectivo")

forma_pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])


cantidad = st.number_input(f"ingrese cantidad de {producto}", 0, step=1)


subtotal= cantidad*precios[pos]
 

descuento = cl.subdescuento(subtotal, forma_pago)
descontado = subtotal - descuento
civa= cl.iva (descontado)
total = round(descontado + civa, 2)
st.write(f"{cliente} su subtotal de {producto} a pagar es de: {subtotal}")

st.write(f"su descuento es de: ${descuento}")

st.write(f"su IVA es de: ${civa}")

st.write(f"su total es de: ${total}")

import pdf_presupuesto
 
archivo = pdf_presupuesto.armar_pdf(
    numero=numero, fecha=fecha, cliente=cliente, producto=producto,
    cantidad=cantidad, precio=precio, subtotal=subtotal,
    descuento=descuento, iva=civa, total=total)
 
st.download_button("Descargar presupuesto (PDF)", archivo,
                   file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")
