import EnhancementCard from "./EnhancementCard";

export default function EnhancementGallery({
    pages,
    selectedVersions,
    onSelectionChange,
}) {

    return (

        <div className="space-y-8">

            {pages.map((page) => (

                <EnhancementCard
                    key={page.page_id}
                    page={page}
                    selectedVersion={selectedVersions[page.page_id] || "enhanced"}
                    onSelectionChange={onSelectionChange}
                />

            ))}

        </div>

    );

}