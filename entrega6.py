#Variables
envio_gratis=0
envio_pago_kg_peso_canastas= 1.20
dinero_canasta = 34 
peso_canasta = 44
total_canasta= envio_pago_kg_peso_canastas

if(dinero_canasta>100):
    print(envio_gratis)

else:
    envio_pago_kg_peso_canastas= peso_canasta * envio_pago_kg_peso_canastas
    total_canasta= envio_pago_kg_peso_canastas + dinero_canasta
    print(total_canasta)


