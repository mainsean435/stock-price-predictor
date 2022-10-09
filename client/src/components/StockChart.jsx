import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import ReactHighcharts from "react-highcharts/ReactHighstock.src"
import moment from "moment"


const StockInfoPage = ({ title }) => {
  const [data, setData] = useState([])
  const { ticker } = useParams()

  useEffect(() => {
    let isMounted = true
    const fetchData = async () => {
      try {
        fetch(`http://127.0.0.1:5000/stocks/${ticker}/data`)
          .then((response) => response.json())
          .then((data) => {
            setData(data);
          });
      } catch (err) {
        console.log(err);
      }
    }
    fetchData()
    return () => (isMounted = false)
  })

  const options = { style: 'currency', currency: 'KES' };
  const numberFormat = new Intl.NumberFormat('en-US', options);
  const config = {
    yAxis: [{
      offset: 20,
      labels: {
        formatter: function () {
          return numberFormat.format(this.value)
        },
        x: -15,
        style: {
          "color": "#000", "position": "absolute"
        },
        align: 'left'
      },
    },
    ],
    tooltip: {
      shared: true,
      formatter: function () {
        return numberFormat.format(this.y, 0) + '</b><br/>' + moment(this.x).format('YYYY-MM-DD')
      }
    },
    plotOptions: {
      series: {
        showInNavigator: true,
        gapSize: 6,
      }
    },
    title: {
      text: title
    },
    chart: {
      height: 600,
    },
    credits: {
      enabled: false
    },
    legend: {
      enabled: true
    },
    xAxis: {
      type: 'date',
    },
    rangeSelector: {
      buttons: [{
        type: 'day',
        count: 7,
        text: '7d'
      }, {
        type: 'month',
        count: 1,
        text: '1m'
      }, {
        type: 'month',
        count: 3,
        text: '3m'
      },
      {
        type: 'year',
        count: 1,
        text: '1y'
      },
      {
        type: 'year',
        count: 5,
        text: '5y'
      },
      {
        type: 'all',
        text: 'Max'
      }],
      selected: 5
    },
    series: [{
      name: 'Price',
      type: 'spline',

      data: data.close,
      tooltip: {
        valueDecimals: 2
      },

    }]
  };
  return (
    <div>
      <ReactHighcharts config={config}></ReactHighcharts>
    </div>
  )
}

export default StockInfoPage

