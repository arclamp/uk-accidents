window.onload = async () => {
  console.log('hello');
  let data = await (await fetch('volume.json')).json();
  console.log(data);

  const div = document.createElement('div');
  document.body.appendChild(div);

  let vis = new components.BarChart(div, {
    data: data,
    x: 'Date',
    y: 'count',
    width: 1920,
    height: 1080,
    renderer: 'svg'
  });
  vis.render();
};
