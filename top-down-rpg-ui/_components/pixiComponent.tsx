import React, { useEffect } from 'react';

import { Application, Assets, Sprite } from 'pixi.js';

const PixiComponent: React.FC = () => {

    const canvasContainerDiv = React.useRef<HTMLDivElement>(null);

    useEffect(() => {
        const app = new Application();
        (async () => {
            await app.init({ background: '#1099bb', resizeTo: window });
            canvasContainerDiv.current?.appendChild(app.canvas);
            const texture = await Assets.load('https://pixijs.com/assets/bunny.png');
            const bunny = new Sprite(texture);
            bunny.anchor.set(0.5);
            bunny.x = app.screen.width / 2;
            bunny.y = app.screen.height / 2;
            app.stage.addChild(bunny);
            app.ticker.add((time) => {
                bunny.rotation += 0.1 * time.deltaTime;
            });
        })();

        return () => {
            app.destroy();
        }
    }, []);
    
    return (
        <div ref={canvasContainerDiv} />
    );
};

export default PixiComponent;