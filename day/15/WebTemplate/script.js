function createPolygon(svg, points) {
    const ns = "http://www.w3.org/2000/svg";
    const polygon = document.createElementNS(ns, "polygon");
    for (value of points) {
        let point = svg.createSVGPoint();
        point.x = value[0];
        point.y = value[1];
        polygon.points.appendItem(point);
    }
    return polygon;
}

function mul(vec, scalar) {
    return [vec[0] * scalar, vec[1] * scalar];
}

function add(sensorPos, d) {
    return [sensorPos[0] + d[0], sensorPos[1] + d[1]];
}

function getPolyPoints(sensorPos, sRadius) {
    const points = [];
    const dirs = [
        [0, -1], [1, 0], [0, 1], [-1, 0]
    ];
    for (let d of dirs) {
        points.push(
            add(sensorPos, mul(d, sRadius))
        );
    }
    return points;
}

function createPolyFromIndex(index, sensors, sensorRadius, svg) {
    const sensorPos = [sensors[index][0][0], sensors[index][0][1]];
    const sRadius = sensorRadius[index];
    const points = getPolyPoints(sensorPos, sRadius);
    const p = createPolygon(svg, points);
    svg.appendChild(p);
}

(() => {

    const svg = document.querySelector("svg");
    const SIZE = 950;

    const sensors = [[[3988693, 3986119], [3979063, 3856315]], [[1129181, 241785], [1973630, -98830]], [[2761889, 2453622], [2803715, 2643139]], [[3805407, 3099635], [3744251, 2600851]], [[3835655, 3999745], [3979063, 3856315]], [[3468377, 3661078], [3979063, 3856315]], [[1807102, 3829998], [2445544, 3467698]], [[2774374, 551040], [1973630, -98830]], [[2004588, 2577348], [2803715, 2643139]], [[2949255, 3611925], [2445544, 3467698]], [[2645982, 3991988], [2445544, 3467698]], [[3444780, 2880445], [3744251, 2600851]], [[3926452, 2231046], [3744251, 2600851]], [[3052632, 2882560], [2803715, 2643139]], [[3994992, 2720288], [3744251, 2600851]], [[3368581, 1443706], [3744251, 2600851]], [[2161363, 1856161], [1163688, 2000000]], [[3994153, 3414445], [3979063, 3856315]], [[2541906, 2965730], [2803715, 2643139]], [[600169, 3131140], [1163688, 2000000]], [[163617, 1082438], [1163688, 2000000]], [[3728368, 140105], [3732654, -724773]], [[1187681, 2105247], [1163688, 2000000]], [[2327144, 3342616], [2445544, 3467698]]];
    
    const sensorRadius = [139434, 1185064, 231343, 559940, 286838, 705923, 1000742, 1450614, 864918, 647938, 724728, 579065, 552006, 488338, 370178, 1532815, 1141514, 456960, 584400, 1694659, 1917633, 869164, 129240, 243482];

    if (true) {
        for (let i = 0; i < sensors.length; i++) {
            let index = i;
            createPolyFromIndex(index, sensors, sensorRadius, svg);
        }
    }

    let index = 0;
    document.addEventListener("keypress", (e) => {
        if (index < sensors.length && e.key == "Enter") {
            createPolyFromIndex(index, sensors, sensorRadius, svg);
            index += 1;
        }
    });
    document.addEventListener("click", (e) => {
        const mPos = {
            x: e.offsetX, 
            y: e.offsetY
        };
        const viewBox = svg.getAttribute("viewBox");
        const viewValues = viewBox.split(" ").map(x => parseInt(x, 10));
        
        const totalSize = viewValues[2] - viewValues[0]; 
        const quarterSize = totalSize / 4;

        mPos.x = mPos.x / SIZE * totalSize + viewValues[0];
        mPos.y = mPos.y / SIZE * totalSize + viewValues[0];

        const n = {
            x1: mPos.x - quarterSize,
            y1: mPos.y - quarterSize,
            x2: mPos.x + quarterSize,
            y2: mPos.y + quarterSize
        };

        const newViewBox = `${n.x1} ${n.y1} ${2 * quarterSize} ${2 * quarterSize}`;

        console.log(mPos);
        //svg.setAttribute("viewBox", newViewBox);
    });

})();