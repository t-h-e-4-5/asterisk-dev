 /* <script>
    document.addEventListener("DOMContentLoaded", () => {
      function fetchData() {
        // Faites une requête AJAX pour récupérer les données de la base de données
        fetch('/find') // Assurez-vous que cette URL correspond à votre route Flask pour récupérer les données
          .then(response => response.json())
          .then(data => {
            const seriesData = [
              {
                name: 'ID',
                data: data.map(entry => entry.id), // Remplacez par le nom réel de la colonne pour les IDs
              },
              {
                name: 'Numero',
                data: data.map(entry => entry.callerId), // Remplacez par le nom réel de la colonne pour les numéros
              },
              {
                name: 'Langues',
                data: data.map(entry => entry.lang), // Remplacez par le nom réel de la colonne pour les langues
              },
              {
                name: 'Parcours',
                data: data.map(entry => entry.parcour), // Remplacez par le nom réel de la colonne pour les parcours
              },
              {
                name: 'Domaines',
                data: data.map(entry => entry.domaine), // Remplacez par le nom réel de la colonne pour les domaines
              },
              {
                name: 'Filieres',
                data: data.map(entry => entry.filiere), // Remplacez par le nom réel de la colonne pour les filières
              },
              {
                name: 'Date',
                data: data.map(entry => entry.date), // Remplacez par le nom réel de la colonne pour les dates
              },
              {
                name: 'Heures',
                data: data.map(entry => entry.hour), // Remplacez par le nom réel de la colonne pour les heures
              },
              {
                name: 'Temps',
                data: data.map(entry => entry.temps), // Remplacez par le nom réel de la colonne pour les temps
              },
            ];

            new ApexCharts(document.querySelector("#reportsChart"), {
              series: seriesData,
              chart: {
                height: 350,
                type: 'area',
                toolbar: {
                  show: false,
                },
              },
              markers: {
                size: 4,
              },
              colors: ['#4154f1', '#2eca6a', '#ff771d'],
              fill: {
                type: "gradient",
                gradient: {
                  shadeIntensity: 1,
                  opacityFrom: 0.3,
                  opacityTo: 0.4,
                  stops: [0, 90, 100],
                },
              },
              dataLabels: {
                enabled: false,
              },
              stroke: {
                curve: 'smooth',
                width: 2,
              },
              xaxis: {
                type: 'datetime',
                categories: data.map(entry => entry.Date), // Remplacez par le nom réel de la colonne pour les dates
              },
              tooltip: {
                x: {
                  format: 'dd/MM/yy HH:mm',
                },
              },
            }).render();
          });
      }

      // Appeler fetchData initialement
      fetchData();

      // Actualiser les données toutes les 5 secondes
      setInterval(fetchData, 5000);
    });
  </script>
*/
<script>
    document.addEventListener("DOMContentLoaded", () => {
      function fetchData() {
        // Faites une requête AJAX pour récupérer les données de la base de données
        fetch('/find') // Assurez-vous que cette URL correspond à votre route Flask pour récupérer les données
          .then(response => response.json())
          .then(data => {
            const seriesData = [
              {
                name: 'ID',
                data: data.map(entry => entry.id), // Remplacez par le nom réel de la colonne pour les IDs
              },
              {
                name: 'Numero',
                data: data.map(entry => entry.callerId), // Remplacez par le nom réel de la colonne pour les numéros
              },
              {
                name: 'Langues',
                data: data.map(entry => entry.lang), // Remplacez par le nom réel de la colonne pour les langues
              },
              {
                name: 'Parcours',
                data: data.map(entry => entry.parcour), // Remplacez par le nom réel de la colonne pour les parcours
              },
              {
                name: 'Domaines',
                data: data.map(entry => entry.domaine), // Remplacez par le nom réel de la colonne pour les domaines
              },
              {
                name: 'Filieres',
                data: data.map(entry => entry.filiere), // Remplacez par le nom réel de la colonne pour les filières
              },
              {
                name: 'Date',
                data: data.map(entry => entry.date), // Remplacez par le nom réel de la colonne pour les dates
              },
              {
                name: 'Heures',
                data: data.map(entry => entry.hour), // Remplacez par le nom réel de la colonne pour les heures
              },
              {
                name: 'Temps',
                data: data.map(entry => entry.temps), // Remplacez par le nom réel de la colonne pour les temps
              },
            ];

            const chartOptions = {
              series: seriesData,
              chart: {
                height: 350,
                type: 'area',
                toolbar: {
                  show: false,
                },
              },
              markers: {
                size: 4,
              },
              colors: ['#4154f1', '#2eca6a', '#ff771d'],
              fill: {
                type: "gradient",
                gradient: {
                  shadeIntensity: 1,
                  opacityFrom: 0.3,
                  opacityTo: 0.4,
                  stops: [0, 90, 100],
                },
              },
              dataLabels: {
                enabled: false,
              },
              stroke: {
                curve: 'smooth',
                width: 2,
              },
              xaxis: {
                type: 'datetime',
                categories: data.map(entry => entry.Date), // Remplacez par le nom réel de la colonne pour les dates
              },
              tooltip: {
                x: {
                  format: 'dd/MM/yy HH:mm',
                },
              },
            };

            // Initialiser le graphique
            new ApexCharts(document.querySelector("#reportsChart"), chartOptions).render();
          });
      }

      // Appeler fetchData initialement
      fetchData();

      // Actualiser les données toutes les 5 secondes
      setInterval(fetchData, 5000);
    });
  </script>