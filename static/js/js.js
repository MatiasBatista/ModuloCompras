
function cambiarPagAlta(){
  window.location.href = "altaContrato.html"
}
function volverMenu(){
  window.location.href = "index.html"
}

function mostrarNombreCereales(){
  selectCereales=document.getElementById('cereales')
  fetch("http://localhost:5000/cereales", {
        method: 'GET', // or 'PUT'
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        cantidadKeysObjeto=Object.keys(data).length
        for (i=0;i<cantidadKeysObjeto;i++){
        const option = document.createElement('option');
        option.text=(data[i]['nombre'].toUpperCase())
        selectCereales.appendChild(option)
        }
    })
    .catch(function(err) {
        console.error(err);
    });
}

function mostrarRazonSocialProveedores(){
  selectProveedores=document.getElementById('proveedores')
  fetch("http://localhost:5000/proveedores", {
        method: 'GET', // or 'PUT'
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        cantidadKeysObjeto=Object.keys(data).length
        for (i=0;i<cantidadKeysObjeto;i++){
        const option = document.createElement('option');
        option.text=(data[i]['razonSocial'].toUpperCase())
        selectProveedores.appendChild(option)
        }
    })
    .catch(function(err) {
        console.error(err);
    });
}

function mostrarLegajoEncargadosCompra(){
  selectEncargados=document.getElementById('encargadosDeCompra')
  fetch("http://localhost:5000/encargadosdecompra", {
        method: 'GET', // or 'PUT'
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        cantidadKeysObjeto=Object.keys(data).length
        for (i=0;i<cantidadKeysObjeto;i++){
        const option = document.createElement('option');
        option.text=(data[i]['legajo'])
        selectEncargados.appendChild(option)
        }
    })
    .catch(function(err) {
        console.error(err);
    });
}

function mostrarNombresIndicadores(){
  selectIndicadores=document.getElementById('indicadores')
  fetch("http://localhost:5000/indicadores", {
        method: 'GET', // or 'PUT'
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        cantidadKeysObjeto=Object.keys(data).length
        for (i=0;i<cantidadKeysObjeto;i++){
          const option = document.createElement('option');
          option.text=(data[i]['nombre'].toUpperCase())
          selectIndicadores.appendChild(option)
        }
    })
    .catch(function(err) {
        console.error(err);
    });
}


function mostrar(){
  console.log(document.getElementById("asd"))
}

function mostrarSelect(){
  console.log(document.getElementById("proveedores"))
  console.log(document.getElementById("proveedores").textContent)
}

function agregarIndicadoresALista(){
    tbody=document.getElementById('tablaIndicadoresCalidad')
    tr=document.createElement('tr')
    td1=document.createElement('td')
    td1.scope="row"
    td1.textContent=document.getElementById('indicadores').value
    tr.appendChild(td1)
    td2=document.createElement('td')
    td2.scope="row"
    td2.textContent=document.getElementById('valorDesdeIndicador').value
    tr.appendChild(td2)
    td3=document.createElement('td')
    td3.scope="row"
    td3.textContent=document.getElementById('valorHastaIndicador').value
    tr.appendChild(td3)
    tbody.appendChild(tr)
  
}

function busquedaProveedor(){
  input=document.getElementById("inputProveedor").value.toUpperCase()
  console.log(input)
  tabla=document.getElementById("myTabla").lastChild
  console.log(tabla)
  for (i=0;i<tabla.childElementCount;i++){
    tr=tabla.childNodes[i]
    console.log(tr)
    td=tr.childNodes[4].textContent.toUpperCase()
    console.log(td)
    console.log(input)
    console.log(td.substring(0,input.length))
    if (td.substring(0,input.length) != input){
      tr.style.display="none";
    }
    else{
      tr.style.display="table-row"
    }
    
  }

}



function busquedaCereal(){
  input=document.getElementById("inputCereal").value.toUpperCase()
  console.log(input)
  tabla=document.getElementById("myTabla").lastChild
  console.log(tabla)
  for (i=0;i<tabla.childElementCount;i++){
    tr=tabla.childNodes[i]
    console.log(tr)
    td=tr.childNodes[3].textContent.toUpperCase()
    console.log(td)
    console.log(input)
    console.log(td.substring(0,input.length))
    if (td.substring(0,input.length) != input){
      tr.style.display="none";
    }
    else{
      tr.style.display="table-row"
    }
    
  }

}

function busquedaEncargadoDeCompras(){
  input=document.getElementById("inputEncargadoDeCompras").value.toUpperCase()
  console.log(input)
  tabla=document.getElementById("myTabla").lastChild
  console.log(tabla)
  for (i=0;i<tabla.childElementCount;i++){
    tr=tabla.childNodes[i]
    console.log(tr)
    td=tr.childNodes[5].textContent.toUpperCase()
    console.log(td)
    console.log(input)
    console.log(td.substring(0,input.length))
    if (td.substring(0,input.length) != input){
      tr.style.display="none";
    }
    else{
      tr.style.display="table-row"
    }
    
  }

}

function busquedaNumeroContrato(){
  input=document.getElementById("inputNumeroContrato").value.toUpperCase()
  console.log(input)
  tabla=document.getElementById("myTabla").lastChild
  console.log(tabla)
  for (i=0;i<tabla.childElementCount;i++){
    tr=tabla.childNodes[i]
    console.log(tr)
    td=tr.childNodes[1].textContent.toUpperCase()
    console.log(td)
    console.log(input)
    console.log(td)
    if (td != input){
      tr.style.display="none";
    }
    else{
      tr.style.display="table-row"
    }
    if (input.length==0){
      tr.style.display="table-row"
    }
    
  }

}


function altaContrato(){
  numero=document.getElementById('numeroContrato').value
  fechaInicio=document.getElementById('fechaInicio').value
  fechaFin=document.getElementById('fechaFin').value
  cereal=document.getElementById('cereales').value
  cantTonelada=document.getElementById('cantidadToneladas').value
  precioPorTonelada=document.getElementById('precioTonelada').value
  cantCamiones=document.getElementById('cantidadCamiones').value
  proveedor=document.getElementById('proveedores').value
  encargadoCompra=document.getElementById('encargadosDeCompra').value
  contadorTr=document.getElementById("tablaIndicadoresCalidad").childNodes.length
  arregloValoresIndicadorCalidad={}

  
  for(i=1;i<contadorTr;i++){
    td=document.getElementById("tablaIndicadoresCalidad").childNodes[i]
    nombre=td.childNodes[0].textContent
    valorDesde=td.childNodes[1].textContent
    valorHasta=td.childNodes[2].textContent
    var valorIndicadorContrato={
      nombreIndicadorCalidad: nombre,
      valorDesde:valorDesde,
      valorHasta:valorHasta
    }
    arregloValoresIndicadorCalidad[i]=valorIndicadorContrato
  }
  console.log(arregloValoresIndicadorCalidad)
  var contrato={

    "numero":numero,
    "cantidadDeToneladas":cantTonelada,
    "precioPorTonelada":precioPorTonelada,
    "cantidadDeCamiones":cantCamiones,
    "fechaInicio":fechaInicio,
    "fechaFin":fechaFin,
    "nombreCereal":cereal,
    "nombreProveedor":proveedor,
    "legajoEncargado":encargadoCompra
  }

  contrato['arregloValoresIndicadorCalidad']=arregloValoresIndicadorCalidad

  fetch("http://localhost:5000/altaContrato", {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify (contrato)
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        alert(data['mensaje'])
        
    })
    .catch(function(err) {
        console.error(err);
    });

  
    
  }
  





function devolverContratos(){

    fetch("http://localhost:5000/contratos", {
        method: 'GET', // or 'PUT'
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then(function(response) {
        return response.json();})
      .then(function(data) {
        cantidadKeysObjeto=Object.keys(data).length
        console.log(cantidadKeysObjeto)
          var html="<thead class='thead-dark'>"
                html+="<tr>"
                html+="<td scope='col'>ID</td>"
                html+="<td scope='col'>NUMERO</td>"
                html+="<td scope='col'>CANTIDAD TONELADAS</td>"
                html+="<td scope='col'>CEREAL</td>"
                html+="<td scope='col'>PROVEEDOR</td>"
                html+="<td scope='col'>ENCARGADO DE COMPRAS</td>"
                html+="</tr>"
                html+="</thead>"
                html+="<tbody>"
          for (let i = 0; i < cantidadKeysObjeto; i++) {
                var id=data[i]['id']
                var numero=data[i]['numero']
                var cantidadToneladas=data[i]['cantidadDeToneladas']
                var nombreCereal=data[i]['nombreCereal']
                var proveedor=data[i]['razonSocialProveedor']
                var encargadoDeCompras=data[i]['nombreEncargadoDeCompras']
                html+="<tr>"
                html+="<td scope='row'>" + id + "</td>"
                html+="<td scope='row'>" + numero+ "</td>"
                html+="<td scope='row'>" + cantidadToneladas + "</td>"
                html+="<td scope='row'>" + nombreCereal.toUpperCase() + "</td>"
                html+="<td scope='row'>" + proveedor.toUpperCase() + "</td>"
                html+="<td scope='row'>" + encargadoDeCompras.toUpperCase()+ "</td>"
                html+=`<td scope='row'width='5%'><button type='button' >Modificar</button></td>`
                html+=`<td scope='row'width='5%'> <button type='button' >Eliminar</button></td>`
                html+="</tr>"
          }
          html+="</tbody>"
          document.getElementById("myTabla").innerHTML=html
    })
    .catch(function(err) {
        console.error(err);
    });

}