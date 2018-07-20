# Fuzzy-String-Matching

We aim at networking and collaboration with history researchers working with digital resources in
Finland. This study describes the aims and the implementation of the project. 

In addition to historians themselves, the digital methods in history research have drawn the attention
of researchers in information studies. Our fields of study include information retrieval and
information behavior. This is an international research effort aiming at supporting digital historians
research work tasks. The context of the research is historian’s research work and we will particularly
focus on (a) research processes and needs descriptions of the historians' work tasks, and (b) the study
the information retrieval in historical document collections, and how to support these with fuzzy
matching methods.

Traditionally, digital access methods in historical research have been studied from the viewpoint of
the document collections and data. Instead of this data-centric view, we adopt information interaction
centered view towards accessing digital collection. Information interaction is understood as
behavioral and cognitive activities related to task planning, searching and selecting information items,
working with information items, and synthetizing and reporting.

Information interaction encompasses searching in the larger task context. This means that the actions
are framed by a motivating task that triggers searching. We aim at better understanding the rationale
behind actions and by this enable combining task-based approach into tool development and
evaluation.

# ABOUT
This repository contains the code to collect .  
The tasks include:
1. collect 
2. Language 
3. Identity 
4. Create
5. Perform 

## Data sources

* [Sotasampo resourse/dataset](http://www.ldf.fi/dataset/warsa)(SPARQL query https://www.w3.org/2009/08/skos-reference/skos.html#)
* [DIGITAALISET AINEISTOT](https://digi.kansalliskirjasto.fi/aikakausi/search)

<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
<svg xmlns='http://www.w3.org/2000/svg' viewBox='20 -5 557 649' xmlns:xlink='http://www.w3.org/1999/xlink' width='557.0px' font-size='12' font-family='Arial, LiberationSans' version='1.1' height='649.0px'>
  <defs>
<style type='text/css'><![CDATA[svg text {text-rendering: geometricPrecision;}]]></style>    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-c2e08f-7ec601' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(194, 224, 143)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(126, 198, 1)'/>
    </linearGradient>
    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-ffffff-b3e0ff' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(255, 255, 255)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(179, 224, 255)'/>
    </linearGradient>
    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-ebe9f9-c1bfea' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(235, 233, 249)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(193, 191, 234)'/>
    </linearGradient>
    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-ff0000-900000' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(255, 0, 0)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(144, 0, 0)'/>
    </linearGradient>
    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-ffffff-f5fffe' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(255, 255, 255)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(245, 255, 254)'/>
    </linearGradient>
    <linearGradient y1='0.0%' x1='0.0%' y2='100.0%' x2='0.0%' id='gradient-fff9c2-ffffff' spreadMethod='pad'>
      <stop stop-opacity='1' offset='0' stop-color='rgb(255, 249, 194)'/>
      <stop stop-opacity='1' offset='100' stop-color='rgb(255, 255, 255)'/>
    </linearGradient>
  </defs>
  <desc>FlowchartDiagram</desc>
  <g transform='translate(262.0,25.0)' id='_dkT3IFq_EDaKK-blC70iAw'>
    <rect rx='20.0' ry='20.0' width='100.0px' stroke-width='1.0' fill='url(#gradient-c2e08f-7ec601)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='18.0' font-size='12' fill='rgb(0, 0, 0)'>Original OCRed</text>
      <text text-anchor='middle' x='50.0' y='30.0' font-size='12' fill='rgb(0, 0, 0)'>letter</text>
    </g>
  </g>
  <g transform='translate(262.0,96.0)' id='_2z_LoFq_EDaKK-blC70iAw'>
    <rect width='100.0px' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(0, 0, 0)'>detect Unicode</text>
    </g>
  </g>
  <g transform='translate(262.0,237.0)' id='_EpzE41rAEDaKK-blC70iAw'>
    <rect width='100.0px' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(0, 0, 0)'>end of line </text>
    </g>
  </g>
  <g transform='translate(262.0,298.0)' id='_KwWMY1rAEDaKK-blC70iAw'>
    <rect width='100.0px' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(0, 0, 0)'>tokenisze</text>
    </g>
  </g>
  <g transform='translate(272.0,381.0)' id='_rKb5IFrAEDaKK-blC70iAw'>
    <polygon stroke-width='1.0' fill='url(#gradient-ebe9f9-c1bfea)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' points='40.0,0.0 0.0,40.0 40.0,80.0 80.0,40.0'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='40.0' y='44.0' font-size='12' fill='rgb(0, 0, 0)'>stem</text>
    </g>
  </g>
  <g transform='translate(462.0,396.0)' id='_1N8lcVrAEDaKK-blC70iAw'>
    <path d='M 0 0 H 55.0 A 12.5 12.5 0 0 1 55 50 H 0 Z' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='40.0' y='23.0' font-size='12' fill='rgb(0, 0, 0)'>remove stop</text>
      <text text-anchor='middle' x='40.0' y='35.0' font-size='12' fill='rgb(0, 0, 0)'>stems </text>
    </g>
  </g>
  <g transform='translate(262.0,504.0)' id='_7ZmPYlrAEDaKK-blC70iAw'>
    <rect width='100.0px' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(0, 0, 0)'>results</text>
    </g>
  </g>
  <g transform='translate(262.0,569.0)' id='_PtsatVrBEDaKK-blC70iAw'>
    <rect rx='20.0' ry='20.0' width='100.0px' stroke-width='1.0' fill='url(#gradient-ff0000-900000)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(255, 255, 255)'>intrepretation</text>
    </g>
  </g>
  <g transform='translate(457.0,81.0)' id='_cykmQFrBEDaKK-blC70iAw'>
    <path d='M 0.0 0.0 H 90.0 V 52.5 Q 69.3 52.5 54.0 59.5 Q 27.0 73.5 0.0 66.5 Z' stroke-width='1.0' fill='url(#gradient-ffffff-f5fffe)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='45.0' y='30.25' font-size='12' fill='rgb(0, 0, 0)'>UTF-8</text>
    </g>
  </g>
  <g transform='translate(50.0,217.0)' id='_im25EFrBEDaKK-blC70iAw'>
    <path d='M 0.0 0.0 H 152.0 V 60.0 Q 117.04 60.0 91.2 68.0 Q 45.6 84.0 0.0 76.0 Z' stroke-width='1.0' fill='url(#gradient-ffffff-f5fffe)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='76.0' y='28.0' font-size='12' fill='rgb(0, 0, 0)'>dash handling, Unicode</text>
      <text text-anchor='middle' x='76.0' y='40.0' font-size='12' fill='rgb(0, 0, 0)'>format</text>
    </g>
  </g>
  <g transform='translate(462.0,278.0)' id='_pMMOUFrBEDaKK-blC70iAw'>
    <path d='M 0.0 0.0 H 80.0 V 60.0 Q 61.6 60.0 48.0 68.0 Q 24.0 84.0 0.0 76.0 Z' stroke-width='1.0' fill='url(#gradient-ffffff-f5fffe)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='40.0' y='28.0' font-size='12' fill='rgb(0, 0, 0)'>remove</text>
      <text text-anchor='middle' x='40.0' y='40.0' font-size='12' fill='rgb(0, 0, 0)'>stopwords</text>
    </g>
  </g>
  <g transform='translate(100.0,564.0)' id='_FfE1IlrCEDaKK-blC70iAw'>
    <path d='M 18.75 0 H 100.0 C 81.25 0.0 81.25 50.0 100.0 50.0  H 18.75 C 0.0 50.0 0.0 0.0 18.75 0.0 ' stroke-width='1.0' fill='url(#gradient-fff9c2-ffffff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='45.3125' y='29.0' font-size='12' fill='rgb(0, 0, 0)'>frequency</text>
    </g>
  </g>
  <g transform='translate(262.0,172.0)' id='_zN6qcG1jEDa2eoXq2cekiA'>
    <rect width='100.0px' stroke-width='1.0' fill='url(#gradient-ffffff-b3e0ff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne' height='40.0px'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='50.0' y='24.0' font-size='12' fill='rgb(0, 0, 0)'>decode</text>
    </g>
  </g>
  <g transform='translate(462.0,152.0)' id='_5EGasW1jEDa2eoXq2cekiA'>
    <path d='M 0.0 0.0 H 80.0 V 60.0 Q 61.6 60.0 48.0 68.0 Q 24.0 84.0 0.0 76.0 Z' stroke-width='1.0' fill='url(#gradient-ffffff-f5fffe)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='40.0' y='28.0' font-size='12' fill='rgb(0, 0, 0)'>clear string</text>
      <text text-anchor='middle' x='40.0' y='40.0' font-size='12' fill='rgb(0, 0, 0)'>form</text>
    </g>
  </g>
  <g transform='translate(112.0,443.0)' id='_YZeiIG1kEDa2eoXq2cekiA'>
    <path d='M 18.75 0 H 100.0 C 81.25 0.0 81.25 50.0 100.0 50.0  H 18.75 C 0.0 50.0 0.0 0.0 18.75 0.0 ' stroke-width='1.0' fill='url(#gradient-fff9c2-ffffff)' fill-opacity='1.0' stroke='rgb(136, 136, 136)' look='allInOne'/>
    <g transform='translate(0.0,0.0)'>
      <text text-anchor='middle' x='45.3125' y='29.0' font-size='12' fill='rgb(0, 0, 0)'>NLP</text>
    </g>
  </g>
  <g transform='translate(312.0,421.0)' id='_wLZ4oFrAEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,81.0)' id='_wuCroVrAEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,288.0)' id='_yomT0FrAEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,421.0)' id='_zqQlJFrAEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(407.0,421.0)' id='_6f-fwVrAEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,483.0)' id='_B2SmAlrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(502.0,495.0)' id='_CqaKkFrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,557.0)' id='_TtFBYVrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(232.0,257.0)' id='_inLpMFrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(412.0,318.0)' id='_pMV_UFrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,360.0)' id='_4xBOIVrBEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(231.0,556.0)' id='_FfMJ4FrCEDaKK-blC70iAw'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(502.0,116.0)' id='_7dCHU2r6EDaiAuZNaGeWcg'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(410.0,116.0)' id='_wYeuY21jEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,154.0)' id='_1nUKwm1jEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(312.0,225.0)' id='_2dLbxm1jEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(502.0,192.0)' id='_5EGatW1jEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(412.0,192.0)' id='_8gCWEW1jEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g transform='translate(237.0,496.0)' id='_cCwV9m1kEDa2eoXq2cekiA'>
    <g transform='translate(0.0,0.0)'/>
  </g>
  <g id='_wLR80lrAEDaKK-blC70iAw'>
    <line y1='421.0' x1='312.0' y2='421.0' x2='312.0' id='_wLVAI1rAEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,421.0) rotate(-0.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_wt6v0lrAEDaKK-blC70iAw'>
    <line y1='65.0' x1='312.0' y2='96.0' x2='312.0' id='_wt9MElrAEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,96.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_yob7w1rAEDaKK-blC70iAw'>
    <line y1='277.0' x1='312.0' y2='298.0' x2='312.0' id='_yoe_ElrAEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,298.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_zqDJwlrAEDaKK-blC70iAw'>
    <line y1='421.0' x1='312.0' y2='421.0' x2='312.0' id='_zqGNEFrAEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,421.0) rotate(-0.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_6fuBEVrAEDaKK-blC70iAw'>
    <line y1='421.0' x1='352.0' y2='421.0' x2='462.0' id='_6fxEY1rAEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(462.0,421.0) rotate(90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_B2G_01rBEDaKK-blC70iAw'>
    <line y1='461.0' x1='312.0' y2='504.0' x2='312.0' id='_B2JcFlrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,504.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_CqOkYVrBEDaKK-blC70iAw'>
    <line y1='446.0' x1='502.0' y2='466.0' x2='502.0' id='_CqRAolrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
  </g>
  <g id='_CqOkYVrBEDaKK-blC70iAw'>
    <line y1='466.0' x1='502.0' y2='524.0' x2='502.0' id='_DzTFQFrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
  </g>
  <g id='_CqOkYVrBEDaKK-blC70iAw'>
    <line y1='524.0' x1='502.0' y2='524.0' x2='362.0' id='_DzTFQVrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(362.0,524.0) rotate(-90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_Ts2X41rBEDaKK-blC70iAw'>
    <line y1='544.0' x1='312.0' y2='569.0' x2='312.0' id='_Ts7QYlrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,569.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_im1D4FrBEDaKK-blC70iAw'>
    <line y1='257.0' x1='262.0' y2='257.0' x2='202.0' id='_inGwslrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(202.0,257.0) rotate(-90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_pMLnRVrBEDaKK-blC70iAw'>
    <line y1='318.0' x1='362.0' y2='318.0' x2='462.0' id='_pMUxMlrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(462.0,318.0) rotate(90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_4wwvc1rBEDaKK-blC70iAw'>
    <line y1='338.0' x1='312.0' y2='381.0' x2='312.0' id='_4wzywlrBEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,381.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_FfE1IVrCEDaKK-blC70iAw'>
    <line y1='544.0' x1='262.0' y2='568.0' x2='200.0' id='_FfK7w1rCEDaKK-blC70iAw' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(200.0,568.0) rotate(-111.16125981682828)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_7cyPsmr6EDaiAuZNaGeWcg'>
    <line y1='116.0' x1='502.0' y2='116.0' x2='502.0' id='_7c1TAmr6EDaiAuZNaGeWcg' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(502.0,116.0) rotate(-0.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_wYHiAW1jEDa2eoXq2cekiA'>
    <line y1='116.0' x1='457.0' y2='116.0' x2='362.0' id='_wYLzdG1jEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(362.0,116.0) rotate(-90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_1nCd821jEDa2eoXq2cekiA'>
    <line y1='136.0' x1='312.0' y2='172.0' x2='312.0' id='_1nHWcm1jEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,172.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_2c-nc21jEDa2eoXq2cekiA'>
    <line y1='212.0' x1='312.0' y2='237.0' x2='312.0' id='_2dBqwG1jEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(312.0,237.0) rotate(-180.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_5EGasG1jEDa2eoXq2cekiA'>
    <line y1='192.0' x1='502.0' y2='192.0' x2='502.0' id='_5EGas21jEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(502.0,192.0) rotate(-0.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_8f0To21jEDa2eoXq2cekiA'>
    <line y1='192.0' x1='362.0' y2='192.0' x2='462.0' id='_8f4lEm1jEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(462.0,192.0) rotate(90.0)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
  <g id='_cChFYG1kEDa2eoXq2cekiA'>
    <line y1='505.0' x1='262.0' y2='486.0' x2='212.0' id='_cCkItW1kEDa2eoXq2cekiA' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)'/>
    <polyline transform='translate(212.0,486.0) rotate(-69.19320898728877)' stroke-width='1.0' fill='none' stroke='rgb(0, 0, 0)' points='-5.0,10.0 0.0,0.0 5.0,10.0'/>
  </g>
</svg>
