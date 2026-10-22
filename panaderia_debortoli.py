import streamlit as st
import calculos as cl

st.title("Panaderia De Bortoli")

productos = ["Chipa", "harina", "medialuna", "Agua 500ml", "criollo"]

cliente = st.text_input ("ingrese su nombre para continuar")
precios = [500, 1000, 700, 1200, 300]
if cliente != "":
    producto1 = st.selectbox("Producto N°1", productos)


pos1 = cl.buscar_posicion(productos, producto1)
precios1 = precios[pos1]
st.write(f"precio por {producto1} = {precios[pos1]}")
cantidad1 = st.number_input(f"ingrese cantidad del 1°er producto: {producto1}", 0, step=1)




producto2 = st.selectbox("Producto N°2", productos)
pos2 = cl.buscar_posicion(productos, producto2)
precios2 = precios[pos2]
st.write(f"precio por {producto2} = {precios[pos2]}")
cantidad2 = st.number_input(f"ingrese cantidad del 2°do producto:{producto2}", 0, step=1)


producto3 = st.selectbox("Producto N°3", productos)
pos3 = cl.buscar_posicion(productos, producto3)
precios3 = precios[pos3]
st.write(f"precio por {producto3} = {precios[pos3]}")
cantidad3 = st.number_input(f"ingrese cantidad del 3°er producto: {producto3}", 0, step=1)


fecha = st.date_input("Fecha")

numero = st.number_input("N° de presupuesto", min_value=1, step=1) 


st.write("obtienes un descuento del 10% al pagar en efectivo")

forma_pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])



subtotal= (cantidad1*precios[pos1]+cantidad2*precios[pos2]+cantidad3*precios[pos3])
 

descuento = cl.subdescuento(subtotal, forma_pago)
descontado = subtotal - descuento
civa= cl.iva (descontado)
total = round(descontado + civa, 2)
st.write(f"{cliente} su subtotal a pagar es de: {subtotal}")

st.write(f"su descuento es de: ${descuento}")

st.write(f"su IVA es de: ${civa}")

st.write(f"su total es de: ${total}")

import pdf_presupuesto
 
archivo = pdf_presupuesto.armar_pdf( numero, fecha, cliente, producto1, producto2, producto3, cantidad1, cantidad2, cantidad3, precios1,precios2,precios3, subtotal, descuento, civa, total)
 
st.download_button("Descargar presupuesto (PDF)", archivo,
                   file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")