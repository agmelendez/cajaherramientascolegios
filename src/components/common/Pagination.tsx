import React, { ReactNode } from 'react';

interface PaginationProps {
  /** Página actual (1-indexed) */
  currentPage: number;
  /** Total de páginas */
  totalPages: number;
  /** Callback cuando cambia la página */
  onChange: (page: number) => void;
  /** Número de botones visibles a cada lado de la página actual */
  siblingCount?: number;
  /** Si está deshabilitado */
  disabled?: boolean;
  /** Clases personalizadas */
  className?: string;
}

/**
 * Componente Pagination para navegación entre páginas
 *
 * @example
 * const [page, setPage] = useState(1);
 * <Pagination
 *   currentPage={page}
 *   totalPages={10}
 *   onChange={setPage}
 * />
 */
export const Pagination: React.FC<PaginationProps> = ({
  currentPage,
  totalPages,
  onChange,
  siblingCount = 1,
  disabled = false,
  className,
}) => {
  const getPageNumbers = (): (number | string)[] => {
    const pages: (number | string)[] = [];

    // Primera página
    pages.push(1);

    // Cálculo de rango alrededor de la página actual
    const leftSibling = Math.max(currentPage - siblingCount, 2);
    const rightSibling = Math.min(currentPage + siblingCount, totalPages - 1);

    // Puntos suspensivos izquierda
    if (leftSibling > 2) {
      pages.push('...');
    }

    // Páginas alrededor de la actual
    for (let i = leftSibling; i <= rightSibling; i++) {
      pages.push(i);
    }

    // Puntos suspensivos derecha
    if (rightSibling < totalPages - 1) {
      pages.push('...');
    }

    // Última página
    if (totalPages > 1) {
      pages.push(totalPages);
    }

    return pages;
  };

  const pages = getPageNumbers();

  return (
    <nav
      className={`flex items-center justify-center gap-1 ${className || ''}`}
      aria-label="Paginación"
    >
      {/* Botón anterior */}
      <button
        onClick={() => onChange(currentPage - 1)}
        disabled={disabled || currentPage === 1}
        className={`
          px-3 py-2 text-sm font-medium rounded
          border border-gray-300
          ${
            disabled || currentPage === 1
              ? 'bg-gray-50 text-gray-400 cursor-not-allowed'
              : 'bg-white text-gray-700 hover:bg-gray-50'
          }
          transition-colors
        `.trim()}
        aria-label="Página anterior"
      >
        ←
      </button>

      {/* Números de página */}
      {pages.map((page, index) => {
        if (page === '...') {
          return (
            <span key={`ellipsis-${index}`} className="px-2 py-2 text-gray-500">
              {page}
            </span>
          );
        }

        const isActive = page === currentPage;

        return (
          <button
            key={page}
            onClick={() => !disabled && onChange(page as number)}
            disabled={disabled}
            className={`
              px-3 py-2 text-sm font-medium rounded
              border transition-colors
              ${
                isActive
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
              }
              ${disabled ? 'cursor-not-allowed opacity-50' : ''}
            `.trim()}
            aria-label={`Ir a página ${page}`}
            aria-current={isActive ? 'page' : undefined}
          >
            {page}
          </button>
        );
      })}

      {/* Botón siguiente */}
      <button
        onClick={() => onChange(currentPage + 1)}
        disabled={disabled || currentPage === totalPages}
        className={`
          px-3 py-2 text-sm font-medium rounded
          border border-gray-300
          ${
            disabled || currentPage === totalPages
              ? 'bg-gray-50 text-gray-400 cursor-not-allowed'
              : 'bg-white text-gray-700 hover:bg-gray-50'
          }
          transition-colors
        `.trim()}
        aria-label="Página siguiente"
      >
        →
      </button>
    </nav>
  );
};

Pagination.displayName = 'Pagination';

export default Pagination;
