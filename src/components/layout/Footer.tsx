import React, { ReactNode } from 'react';

interface FooterProps {
  /** Contenido del footer */
  children?: ReactNode;
  /** Si el footer es sticky (fijo al fondo) */
  sticky?: boolean;
}

/**
 * Componente Footer de la aplicación
 */
export const Footer: React.FC<FooterProps> = ({ children, sticky = false }) => {
  return (
    <footer
      className={`
        ${sticky ? 'sticky' : 'static'} bottom-0 left-0 right-0
        bg-gray-900 text-white
        py-8 px-4 md:px-6
      `.trim()}
    >
      <div className="max-w-7xl mx-auto">
        {children ? (
          children
        ) : (
          /* Default footer content */
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
            {/* Sección 1: Acerca de */}
            <div>
              <h3 className="font-semibold text-lg mb-4">Caja de Herramientas</h3>
              <p className="text-gray-400 text-sm">
                Plataforma de autoformación docente en IA para el MEP
              </p>
            </div>

            {/* Sección 2: Enlaces rápidos */}
            <div>
              <h4 className="font-semibold mb-4">Enlaces Rápidos</h4>
              <ul className="space-y-2 text-sm">
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Documentación
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Soporte
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Contacto
                  </a>
                </li>
              </ul>
            </div>

            {/* Sección 3: Legal */}
            <div>
              <h4 className="font-semibold mb-4">Legal</h4>
              <ul className="space-y-2 text-sm">
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Privacidad
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Términos de servicio
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    RGPD
                  </a>
                </li>
              </ul>
            </div>
          </div>
        )}

        {/* Separador */}
        <div className="border-t border-gray-700 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-gray-400">
            <p>&copy; 2026 Ministerio de Educación Pública. Todos los derechos reservados.</p>
            <div className="flex gap-6">
              <a href="#" className="hover:text-white transition-colors">
                Política de privacidad
              </a>
              <a href="#" className="hover:text-white transition-colors">
                Términos
              </a>
              <a href="#" className="hover:text-white transition-colors">
                Contacto
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

Footer.displayName = 'Footer';

export default Footer;
